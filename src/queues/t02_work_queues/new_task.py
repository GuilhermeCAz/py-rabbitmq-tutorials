import sys

import pika


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)

        message = ' '.join(sys.argv[1:]) or 'Hello World!'
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent,
            ),
        )
        print(f' [x] Sent {message}')


if __name__ == '__main__':
    main()
