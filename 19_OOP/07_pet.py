class Pet:
    #class attribute
    allowed = ["dog", "cat", "bird", "fish"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet. Allowed species are: {', '.join(Pet.allowed)}")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet. Allowed species are: {', '.join(Pet.allowed)}")
        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Buddy", "dog")

print(cat.name, cat.species)
print(dog.name, dog.species)
# print(tiger.name, tiger.species)  # Raises a ValueError;
# print(cat.set_species("tiger"));
print(id(cat.allowed))  # The allowed list is shared between instances of Pet class,);

cat.allowed = ['tiger', 'bear'] # creates an instance of the allowed list on the cat object
print(cat.allowed)
print(Pet.allowed);