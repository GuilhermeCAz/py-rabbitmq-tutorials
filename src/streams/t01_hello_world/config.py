import os

from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_STREAM_PORT = int(os.getenv('RABBITMQ_STREAM_PORT', '5552'))
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
