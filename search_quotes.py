import re
import redis
from models.main_models import Quote


r = redis.Redis(host='localhost', port=6379, db=0)

def search_quotes(command):
    if command.startswith('name:'):
        name = command[5:]
        cache_key = f'name:{name}'
        cached_result = r.get(cache_key)
        
        if cached_result:
            return cached_result.decode('utf-8').split(',')

        regex = re.compile(name, re.IGNORECASE)
        quotes = Quote.objects(author__fullname=regex)
        result = [quote.quote for quote in quotes]
        r.set(cache_key, ','.join(result))
        return result
    
    elif command.startswith('tag:'):
        tag = command[4:]
        cache_key = f'tag:{tag}'
        cached_result = r.get(cache_key)

        if cached_result:
            return cached_result.decode('utf-8').split(',')

        quotes = Quote.objects(tags=tag)
        result = [quote.quote for quote in quotes]
        r.set(cache_key, ','.join(result))
        return result
    
    elif command.startswith('tags:'):
        tags = command[5:].split(',')
        quotes = Quote.objects(tags__in=tags)
        return [quote.quote for quote in quotes]

    elif command == 'exit':
        return 'exit'

def main():
    while True:
        command = input("Enter command: ")
        result = search_quotes(command)
        if result == 'exit':
            break
        print(result)

if __name__ == '__main__':
    main()
