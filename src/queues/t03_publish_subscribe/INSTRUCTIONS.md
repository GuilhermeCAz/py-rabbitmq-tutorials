# Tutorial 03: Publish/Subscribe

<https://www.rabbitmq.com/tutorials/tutorial-three-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   python receive_logs.py
   ```

   Terminal 2 (sender):

   ```bash
   python emit_logs.py
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
