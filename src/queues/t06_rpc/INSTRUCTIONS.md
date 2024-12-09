# Tutorial 06: Remote procedure call (RPC)

<https://www.rabbitmq.com/tutorials/tutorial-six-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   cd src/queues/t06_rpc
   python rpc_server.py
   ```

   Terminal 2 (sender):

   ```bash
   cd src/queues/t06_rpc
   python rpc_client.py
   ```

### Expected outputs

Server:

```text
 [x] Awaiting RPC requests
 [.] fib(30)
```

Client:

```text
 [x] Requesting fib(30)
 [.] Got 832040
```
