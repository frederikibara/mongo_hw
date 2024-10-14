from mongoengine import Document, StringField, DateTimeField, ListField, ReferenceField, connect

connect('homework8', host='mongodb+srv://fredderf:fred555@cluster0.a03do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)


# MONGODB_URI = "mongodb+srv://fredderf:fred555@cluster0.a03do.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" 
# redis = "redis://localhost:6379/"
# Rtabbit = "amqp://guest:guest@localhost:5672/"