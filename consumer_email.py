import pika
from models.contact_model import Contact

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects.get(id=contact_id)
    print(f"Sending email to {contact.email}")
    contact.sent = True
    contact.save()

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for emails...')
    channel.start_consuming()

if __name__ == '__main__':
    consume()
