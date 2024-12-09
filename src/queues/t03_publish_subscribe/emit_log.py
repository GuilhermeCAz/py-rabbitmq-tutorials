import sys

import pika


def main() -> None:
    with pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'),
    ) as connection:
        channel = connection.channel()

        channel.exchange_declare(exchange='logs', exchange_type='fanout')

        message = ' '.join(sys.argv[1:]) or 'info: Hello World!'
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(f' [x] Sent {message}')


if __name__ == '__main__':
    main()
