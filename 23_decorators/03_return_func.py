from random import choice

# We can return funcs from other funcs
def make_laugh_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f"{laugh} {person}"
    
    return get_laugh

# laugh = make_laugh_func()
# print(laugh());

laugh_at = make_laugh_func("Marion")

print(laugh_at());
print(laugh_at());
print(laugh_at());
print(laugh_at());
print(laugh_at());