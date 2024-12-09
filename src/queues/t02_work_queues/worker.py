import time

import pika


def callback(
    ch: pika.adapters.blocking_connection.BlockingChannel,
    method: pika.spec.Basic.Deliver,
    _properties: pika.BasicProperties,
    body: bytes,
) -> None:
    print(f' [x] Received {body.decode()}')
    time.sleep(body.count(b'.'))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='task_queue', on_message_callback=callback)

        channel.start_consuming()


if __name__ == '__main__':
    main()
