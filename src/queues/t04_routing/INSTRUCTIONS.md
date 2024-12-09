# Tutorial 04: Routing

<https://www.rabbitmq.com/tutorials/tutorial-four-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   cd src/queues/t04_routing
   python receive_logs_direct.py info warning error
   ```

   Terminal 2 (sender):

   ```bash
   cd src/queues/t04_routing
   python emit_log_direct.py error "Run. Run. Or it will explode."
   ```

### Expected outputs

Receiver:

```text
 [*] Waiting for logs. To exit press CTRL+C
 [x] error: Run. Run. Or it will explode.
```

Sender:

```text
 [x] Sent error: Run. Run. Or it will explode.
```
