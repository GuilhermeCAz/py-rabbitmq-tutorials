import asyncio
import sys

from config import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_STREAM_PORT,
    RABBITMQ_USERNAME,
)
from rstream import (
    AMQPMessage,
    Consumer,
    ConsumerOffsetSpecification,
    MessageContext,
    OffsetNotFound,
    OffsetType,
    ServerError,
    amqp_decoder,
)

STREAM_NAME = 'stream-offset-tracking-python'
STREAM_RETENTION = 2000000000  # 2GB


class StreamOffsetTracker:
    def __init__(self) -> None:
        self.message_count = -1
        self.first_offset = -1
        self.last_offset = -1

    async def on_message(
        self,
        msg: AMQPMessage,
        message_context: MessageContext,
    ) -> None:
        offset = message_context.offset
        if self.first_offset == -1:
            print('First message received')
            self.first_offset = offset

        consumer = message_context.consumer
        stream = consumer.get_stream(
            message_context.subscriber_name,
        )

        # Store the offset after every 10 messages received
        self.message_count += 1

        if self.message_count % 10 == 0:
            await consumer.store_offset(
                stream=stream,
                offset=offset,
                subscriber_name=message_context.subscriber_name,
            )

        if 'marker' in str(msg):
            await consumer.store_offset(
                stream=stream,
                offset=offset,
                subscriber_name=message_context.subscriber_name,
            )
            self.last_offset = offset
            await consumer.close()

    async def consume(self) -> None:
        stored_offset = -1

        consumer = Consumer(
            RABBITMQ_HOST,
            port=RABBITMQ_STREAM_PORT,
            username=RABBITMQ_USERNAME,
            password=RABBITMQ_PASSWORD,
        )

        await consumer.create_stream(
            STREAM_NAME,
            exists_ok=True,
            arguments={'max-length-bytes': STREAM_RETENTION},
        )

        try:
            await consumer.start()
            print('Started consuming: Press Ctrl+C to close')
            try:
                # Will raise an exception if store_offset wasn't invoked before
                stored_offset = await consumer.query_offset(
                    stream=STREAM_NAME,
                    subscriber_name='subscriber_1',
                )
            except OffsetNotFound as offset_exception:
                print(f'Offset not previously stored. {offset_exception}')

            except ServerError as server_error:
                print(f'Server error: {server_error}')
                sys.exit(1)

            # If no offset was previously stored, start from the first offset
            stored_offset += 1
            await consumer.subscribe(
                stream=STREAM_NAME,
                subscriber_name='subscriber_1',
                callback=self.on_message,
                decoder=amqp_decoder,
                offset_specification=ConsumerOffsetSpecification(
                    OffsetType.OFFSET,
                    stored_offset,
                ),
            )
            await consumer.run()

        except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
            await consumer.close()

        # Give time to the consumer task to close the consumer
        await asyncio.sleep(1)

        if self.first_offset != -1:
            print(
                f'Done consuming first_offset: {self.first_offset} '
                f'last_offset {self.last_offset} ',
            )


if __name__ == '__main__':
    tracker = StreamOffsetTracker()
    with asyncio.Runner() as runner:
        runner.run(tracker.consume())
