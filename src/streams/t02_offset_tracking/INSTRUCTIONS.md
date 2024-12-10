# Tutorial 02: Offset Tracking

<https://www.rabbitmq.com/tutorials/tutorial-two-python-stream>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   python offset_tracking_receive.py
   ```

   Terminal 2 (sender):

   ```bash
   python offset_tracking_send.py
   ```

### Expected outputs

Receiver:

```text
Started consuming: Press Ctrl+C to close
First message received.
Done consuming, first offset 0, last offset 99.
```

Sender:

```text
Publishing 100 messages
Messages confirmed: true
```
