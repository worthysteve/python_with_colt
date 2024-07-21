
#! Inheritance example: User and Moderator
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
        return f"Happy {self.age}th, {self.first}! You are now {self.age} years old."

class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods +=1
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active moderators."

    def remove_post(self):
        return f"{self.full_name} removed a post from {self.community}"

# print(User.display_active_users());
# u1 = User("Tom", "Garcia", 35)
# print(User.display_active_users());
# jasmine = Moderator("Jasmine", "O'conner", 61, 'Piano')
# print(User.display_active_users());

u1 = User("Tom", "Garcia", 35)
u1 = User("Donald", "Trump", 80)
u1 = User("Julius Maada", "Bio", 55)
jasmine = Moderator("Jasmine", "O'conner", 61, 'Piano')
umu = Moderator("Umu-Hawa", "Barrie", 24, 'Computer Science')
print(User.display_active_users());
print(Moderator.display_active_mods());
