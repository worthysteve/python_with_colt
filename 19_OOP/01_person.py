class User:
    def __init__(self, first, last, age):
        # print("A NEW USER HAS BEEN MADE");
        self.first = first  
        self.last = last  
        self.age = age
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}. {self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th Birthday, {self.first}! You are now {self.age} years old."

user1 = User('Steven', 'Daniel', 28)
user2 = User("Umu", "Barrie", 24)
user3 = User('Becky', 'Kaimbay', 29)
# print(user1);
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user3.first, user3.last, user3.age)

print(user1.full_name())
print(user2.initials());
print(user3.likes('reading'))
print(user1.is_senior());
print(user2.birthday());
