import asyncio

from rstream import (
    AMQPMessage,
    Consumer,
    ConsumerOffsetSpecification,
    MessageContext,
    OffsetType,
)

STREAM_NAME = 'hello-python-stream'
STREAM_RETENTION = 5000000000  # 5GB


async def on_message(
    msg: AMQPMessage,
    message_context: MessageContext,
) -> None:
    stream = message_context.consumer.get_stream(
        message_context.subscriber_name,
    )
    print(f'Got message: {msg.decode()} from stream {stream}')


async def receive() -> None:
    async with Consumer(
        host='localhost',
        username='guest',
        password='guest',  # noqa: S106
    ) as consumer:
        await consumer.create_stream(
            STREAM_NAME,
            exists_ok=True,
            arguments={'max-length-bytes': STREAM_RETENTION},
        )

        print('Press control + C to close')
        await consumer.start()
        await consumer.subscribe(
            stream=STREAM_NAME,
            callback=on_message,
            offset_specification=ConsumerOffsetSpecification(
                OffsetType.FIRST,
                None,
            ),
        )
        try:
            await consumer.run()
        except (KeyboardInterrupt, asyncio.CancelledError):
            print('Closing Consumer...')
            return


def main() -> None:
    with asyncio.Runner() as runner:
        runner.run(receive())


if __name__ == '__main__':
    main()
