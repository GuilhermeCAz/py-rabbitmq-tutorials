import pika


def callback(
    _ch: pika.adapters.blocking_connection.BlockingChannel,
    _method: pika.spec.Basic.Deliver,
    _properties: pika.BasicProperties,
    body: bytes,
) -> None:
    """Callback function for consuming messages from a queue.

    Args:
        _ch (pika.adapters.blocking_connection.BlockingChannel):
            The channel object.
        _method (pika.spec.Basic.Deliver):
            Delivery method.
        _properties (pika.BasicProperties):
            Properties associated with the message.
        body (bytes):
            The message body received from the queue.
    """
    print(f' [x] Received {body.decode()}')


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_consume(
            queue='hello',
            on_message_callback=callback,
            auto_ack=True,
        )

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


if __name__ == '__main__':
    main()
