import sys

import pika


def callback(
    _ch: pika.adapters.blocking_connection.BlockingChannel,
    method: pika.spec.Basic.Deliver,
    _properties: pika.BasicProperties,
    body: bytes,
) -> None:
    print(f' [x] {method.routing_key}: {body.decode()}')


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.exchange_declare(
            exchange='direct_logs',
            exchange_type='direct',
        )

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        severities = sys.argv[1:]
        if not severities:
            sys.stderr.write(
                f'Usage: {sys.argv[0]} [info] [warning] [error]\n',
            )
            sys.exit(1)

        for severity in severities:
            channel.queue_bind(
                exchange='direct_logs',
                queue=queue_name,
                routing_key=severity,
            )

        print(' [*] Waiting for logs. To exit press CTRL+C')

        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

        channel.start_consuming()


if __name__ == '__main__':
    main()
