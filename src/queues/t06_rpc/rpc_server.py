import pika


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def on_request(
    ch: pika.adapters.blocking_connection.BlockingChannel,
    method: pika.spec.Basic.Deliver,
    props: pika.BasicProperties,
    body: bytes,
) -> None:
    """
    Process an RPC request.

    Process a request by calculating the Fibonacci number for the given
    argument, and then respond with the result.

    Args:
        ch: The channel object.
        method: Delivery method.
        props: Properties associated with the message.
        body: The message body received from the queue.
    """
    n = int(body)

    print(f' [.] fib({n})')
    response = fib(n)

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='rpc_queue')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue='rpc_queue',
            on_message_callback=on_request,
        )

        print(' [x] Awaiting RPC requests')
        channel.start_consuming()


if __name__ == '__main__':
    main()
