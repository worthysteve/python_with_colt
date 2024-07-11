class User:
    def __init__(self, first, last, age):
        # print("A NEW USER HAS BEEN MADE");
        self.first = first  # Change name to first to match the attribute name
        self.last = last  # Correct the typo from '-' to '='
        self.age = age

user1 = User('Steven', 'Daniel', 28)
user2 = User("Umu", "Barrie", 24)
user3 = User('Becky', 'Kaimbay', 29)
# print(user1);
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)
print(user3.first, user3.last, user3.age)
