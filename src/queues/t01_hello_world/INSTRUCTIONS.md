# Tutorial 01: Hello World

<https://www.rabbitmq.com/tutorials/tutorial-one-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   python receive.py
   ```

   Terminal 2 (sender):

   ```bash
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
