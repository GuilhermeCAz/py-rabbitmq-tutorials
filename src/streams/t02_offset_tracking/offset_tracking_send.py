import asyncio

from config import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_STREAM_PORT,
    RABBITMQ_USERNAME,
)
from rstream import AMQPMessage, ConfirmationStatus, Producer

STREAM = 'stream-offset-tracking-python'
MESSAGES = 100
STREAM_RETENTION = 2000000000  # 2GB


class MessagePublisher:
    def __init__(self) -> None:
        self.confirmed_messages = 0
        self.all_confirmed_messages_cond = asyncio.Condition()

    async def on_publish_confirm(
        self,
        confirmation: ConfirmationStatus,
    ) -> None:
        if confirmation.is_confirmed:
            self.confirmed_messages += 1
            if self.confirmed_messages == MESSAGES:
                async with self.all_confirmed_messages_cond:
                    self.all_confirmed_messages_cond.notify()

    async def publish(self) -> None:
        async with Producer(
            RABBITMQ_HOST,
            port=RABBITMQ_STREAM_PORT,
            username=RABBITMQ_USERNAME,
            password=RABBITMQ_PASSWORD,
        ) as producer:
            # Create a stream if it doesn't already exist
            await producer.create_stream(
                STREAM,
                exists_ok=True,
                arguments={'max-length-bytes': STREAM_RETENTION},
            )

            print(f'Publishing {MESSAGES} messages')

            # Send 99 hello messages
            for i in range(MESSAGES - 1):
                amqp_message = AMQPMessage(
                    body=bytes(f'hello: {i}', 'utf-8'),
                )

                await producer.send(
                    stream=STREAM,
                    message=amqp_message,
                    on_publish_confirm=self.on_publish_confirm,
                )

            # Send a final marker message
            amqp_message = AMQPMessage(
                body=bytes(f'marker: {i + 1}', 'utf-8'),
            )

            await producer.send(
                stream=STREAM,
                message=amqp_message,
                on_publish_confirm=self.on_publish_confirm,
            )

            # Wait for all messages to be confirmed
            async with self.all_confirmed_messages_cond:
                await self.all_confirmed_messages_cond.wait()

            print('Messages confirmed: true')


if __name__ == '__main__':
    publisher = MessagePublisher()
    asyncio.run(publisher.publish())
