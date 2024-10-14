import json
from models.main_models import Author, Quote

def load_authors():
    with open('data/authors.json') as f:
        authors = json.load(f)
        for author in authors:
            Author(**author).save()

def load_quotes():
    with open('data/qoutes.json') as f:
        quotes = json.load(f)
        for quote in quotes:
            author = Author.objects(fullname=quote['author']).first()
            Quote(tags=quote['tags'], author=author, quote=quote['quote']).save()

if __name__ == '__main__':
    load_authors()
    load_quotes()
