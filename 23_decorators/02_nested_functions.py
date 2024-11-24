# We can nest functions inside another function

from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there', 'Go away', 'I love you '))
        return msg
    
    result = get_mood() + person
    return result

print(greet(" Steven"));