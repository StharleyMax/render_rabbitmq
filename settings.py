from decouple import config

RABBITMQ_HOST = config('RABBITMQ_HOST', default='')
RABBITMQ_PORT = config('RABBITMQ_PORT', default='')
RABBITMQ_USERNAME = config('RABBITMQ_USERNAME', default='')
RABBITMQ_PASSWORD = config('RABBITMQ_PASSWORD', default='')
RABBITMQ_URI = (
    f'amqps://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}' f'/{RABBITMQ_USERNAME}'
)
