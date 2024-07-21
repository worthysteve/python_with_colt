
#! the super() keyword

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}");

class Cat(Animal):
    def __init__(self, name, breed, toy):
        # self.name = name # duplication, it goes against inheritance
        # self.species = species # duplication, it goes against inheritance

        super().__init__(name, species="Cat") # Inheritance
        # Animal.__init__(self, name, species) # inheritance
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}");

blue = Cat("Blue", "Scottish fold", "String")
# blue.make_sound("MEOW")
# print(blue.cool);
# print(Cat.cool);
# print(Animal.cool);
print(blue);
print(blue.species);
print(blue.breed);
print(blue.toy);
blue.play()


# print(isinstance(blue, Cat)) # True
# print(isinstance(blue, Animal)) #True
# print(isinstance(blue, object)) #True