"""
#! MRO Genetics
Do you remember Gregor Mendel  from biology? We're going to simulate basic Mendelian inheritance in this exercise. You don't need to know what that means, but basically imagine a family where all the kids look exactly like one parent, maybe that parent has more "dominant" genetic traits than the other parent.

Create three classes, Mother , Father , and Child .

Let Mother have the "dominant" traits:

eye_color = "brown"
hair_color = "dark brown"
hair_type = "curly"
Let Father  have "recessive" traits:

eye_color = "blue"
hair_color = "blond"
hair_type = "straight"


Now define Child  to have the same attributes, eye_color , hair_color , and hair_type , but don't set them on the class.  Instead, let Child's Method Resolution Order be such that Child inherits from Mother  first, then Father .

Note: You don't have to instantiate any of the classes to pass the tests. The tests will create instances for you.

"""
# Define your classes below:
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"

class Child(Mother, Father):
    pass
