
#! MULTIPLE INHERITANCE
class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT");
        self.name = name

    def swim(self):
        return f"{self.name} is swimming!"
    
    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT");
        self.name = name
        
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT");
        super().__init__(name=name)

# jaws = Aquatic("Jaws")
# lassie = Ambulatory ("Lassie")
captain_cook = Penguin ("Captain Cook") # Prints only the AMBULATORY AND PENGUIN INIT, this is because of their positioning in the Penguin class 
print(captain_cook.walk());
print(captain_cook.swim());
print(captain_cook.greet()); # prints the greet() of the Ambulatory class

print(f"{captain_cook.name} is an instance of Penguin: {isinstance(captain_cook, Penguin)}");

print(f"{captain_cook.name} is an instance of Aquatic: {isinstance(captain_cook, Aquatic)}");

print(f"{captain_cook.name} is an instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}");
print(f"{captain_cook.name} is an instance of Object: {isinstance(captain_cook, object)}");