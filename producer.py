import random
import pika
from models.contact_model import Contact

def generate_contacts(count):
    for _ in range(count):
        contact = Contact(
            fullname=f'Contact {_}',
            email=f'contact{_}@example.com',
            phone=f'123-456-7890',
            preferred_method=random.choice(['email', 'sms'])
        )
        contact.save()
        send_to_queue(contact.id)

def send_to_queue(contact_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    channel.queue_declare(queue='sms_queue')

    contact = Contact.objects.get(id=contact_id)
    queue_name = 'email_queue' if contact.preferred_method == 'email' else 'sms_queue'
    channel.basic_publish(exchange='', routing_key=queue_name, body=str(contact_id))
    connection.close()

if __name__ == '__main__':
    generate_contacts(10)  
