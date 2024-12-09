import sys

import pika


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'  # noqa: PLR2004
        message = ' '.join(sys.argv[2:]) or 'Hello World!'
        channel.basic_publish(
            exchange='topic_logs',
            routing_key=routing_key,
            body=message,
        )
        print(f' [x] Sent {routing_key}: {message}')


if __name__ == '__main__':
    main()
