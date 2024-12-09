# Tutorial 01: Hello World

<https://www.rabbitmq.com/tutorials/tutorial-one-python-stream>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (sender):

   ```bash
   cd src/streams/t00_hello_world
   python send.py
   ```

   Terminal 2 (receiver):

   ```bash
   cd src/streams/t00_hello_world
   python receive.py
   ```

### Expected outputs

Sender:

```text
 [x] Hello, World! message sent
 [x] Press Enter to close the producer  ...
```

Receiver:

```text
Press control + C to close
Got message: Hello, World! from stream hello-python-stream
```
