import asyncio

from rstream import Producer

from streams.t02_offset_tracking.config import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_STREAM_PORT,
    RABBITMQ_USERNAME,
)

STREAM_NAME = 'hello-python-stream'
STREAM_RETENTION = 5000000000  # 5GB


async def send() -> None:
    async with Producer(
        RABBITMQ_HOST,
        port=RABBITMQ_STREAM_PORT,
        username=RABBITMQ_USERNAME,
        password=RABBITMQ_PASSWORD,
    ) as producer:
        await producer.create_stream(
            STREAM_NAME,
            exists_ok=True,
            arguments={'max-length-bytes': STREAM_RETENTION},
        )

        await producer.send(stream=STREAM_NAME, message=b'Hello, World!')

        print(' [x] Hello, World! message sent')

        input(' [x] Press Enter to close the producer  ...')


def main() -> None:
    with asyncio.Runner() as runner:
        runner.run(send())


if __name__ == '__main__':
    main()
