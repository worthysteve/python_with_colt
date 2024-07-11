class Person:
    def __init__(self):
        self.name = "Steven"
        self._secret = "This is a secret"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         return "Access granted"
    #     else:
    #         return "Access denied"
        self.__msg = "This is a private message"


p = Person()

print(p.name);
print(p._secret)
print(p._Person__msg);
