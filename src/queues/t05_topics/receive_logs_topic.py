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

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

        result = channel.queue_declare('', exclusive=True)
        queue_name = result.method.queue

        binding_keys = sys.argv[1:]
        if not binding_keys:
            sys.stderr.write(f'Usage: {sys.argv[0]} [binding_key]...\n')
            sys.exit(1)

        for binding_key in binding_keys:
            channel.queue_bind(
                exchange='topic_logs',
                queue=queue_name,
                routing_key=binding_key,
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
