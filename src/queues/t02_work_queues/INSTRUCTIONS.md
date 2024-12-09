# Tutorial 02: Work Queues

<https://www.rabbitmq.com/tutorials/tutorial-two-python>

## Instructions

1. Ensure RabbitMQ server is running.

2. You need three consoles open. Two will run the worker.py script. These consoles will be our two consumers - C1 and C2.

   ```bash
   # shell 1
   python worker.py
   # => [*] Waiting for messages. To exit press CTRL+C
   ```

   ```bash
   # shell 2
   python worker.py
   # => [*] Waiting for messages. To exit press CTRL+C
   ```

3. In the third one we'll publish new tasks. Once you've started the consumers you can publish a few messages:

   ```bash
   # shell 3
   python new_task.py First message.
   python new_task.py Second message..
   python new_task.py Third message...
   python new_task.py Fourth message....
   python new_task.py Fifth message.....
   ```

### Expected outputs

```bash
# shell 1
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'First message.'
# => [x] Received 'Third message...'
# => [x] Received 'Fifth message.....'
```

```bash
# shell 2
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'Second message..'
# => [x] Received 'Fourth message....'
```
