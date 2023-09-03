import pika
from settings import RABBITMQ_URI, RABBITMQ_PORT


def my_callback(ch, method, properties, body):
    print(body)

connection_parameters = pika.URLParameters(url=RABBITMQ_URI)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(queue="data_queue", durable=True)
channel.basic_consume(queue="data_queue", auto_ack=True, on_message_callback=my_callback)

print(f'Listem on port {RABBITMQ_PORT}')

channel.start_consuming()
