class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        # print("A NEW USER HAS BEEN MADE");
        self.first = first  
        self.last = last  
        self.age = age
        User.active_users += 1  # Increment the active_users count by 1 each time a new User object is created. # This counts the total number of active User objects created.
    
    def logout(self):
        User.active_users -= 1  # Decrement the active_users count by 1 when a User object is logged out. # This counts the total number of active User objects created.    
        return f"{self.first} has logged out."
    
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

# print(user1);
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user3.first, user3.last, user3.age)

# print(user1.full_name())
# print(user2.initials());
# print(user3.likes('reading'))
# print(user1.is_senior());
# print(user2.birthday());

print(User.active_users)
user1 = User('Steven', 'Daniel', 28)
user2 = User("Umu", "Barrie", 24)
user3 = User('Becky', 'Kaimbay', 29)
print(User.active_users)
print(user1.logout())
print(User.active_users)

print(User.display_active_users())

user1 = User('Steven', 'Daniel', 28)
user2 = User("Umu", "Barrie", 24)
user3 = User('Becky', 'Kaimbay', 29)
print(User.display_active_users())

steve = User.from_string('Steven,Daniel,28')
print(steve.first)
print(steve.full_name())
print(steve.birthday());
