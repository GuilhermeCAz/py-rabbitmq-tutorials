# Tutorial 01: Hello World

<https://www.rabbitmq.com/tutorials/tutorial-one-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   cd src/queues/t00_hello_world
   python receive.py
   ```

   Terminal 2 (sender):

   ```bash
   cd src/queues/t00_hello_world
   python send.py
   ```

### Expected outputs

Receiver:

```text
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received 'Hello World!'
```

Sender:

```text
 [x] Sent 'Hello World!'
```
