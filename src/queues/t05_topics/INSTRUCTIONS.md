# Tutorial 05: Topics

<https://www.rabbitmq.com/tutorials/tutorial-five-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. Open two terminals:

   Terminal 1 (receiver):

   ```bash
   cd src/queues/t05_topics

   # To receive all the logs run:
   python receive_logs_topic.py "#"

   # To receive all logs from the facility kern:
   python receive_logs_topic.py "kern.*"

   # Or if you want to hear only about critical logs:
   python receive_logs_topic.py "*.critical"

   # You can create multiple bindings:
   python receive_logs_topic.py "kern.*" "*.critical"
   ```

   Terminal 2 (sender):

   ```bash
   cd src/queues/t05_topics
   # To emit a log with a routing key kern.critical type:
   python emit_log_topic.py "kern.critical" "A critical kernel error"
   ```

### Expected outputs

Receiver:

```text
 [*] Waiting for logs. To exit press CTRL+C
 [x] kern.critical: A critical kernel error
```

Sender:

```text
 [x] Sent kern.critical: A critical kernel error
```
