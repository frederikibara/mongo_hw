from mongoengine import Document, StringField, BooleanField, connect

connect('homework8', host='mongodb+srv://fredderf:fred555@cluster0.a03do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)
    phone = StringField()
    preferred_method = StringField(choices=['email', 'sms'])
