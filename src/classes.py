# CB 1st Classes Notes


# Example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"Name = {self.name}\nSpecies = {self.species}\nAge = {self.age}"
    
    def birthday(self):
        self.age += 1

dog = Animal("Doug","dog",4)

for k,v in vars(dog).items():
    print(f"{k.capitalize()}: {v}")

print("\n")

print(dog)

dog.birthday()

print(dog)

# Example 2
class ClassPeriod:
    def __init__(self,subject,teacher = "Ms. LaRose",room = None):
        self.subject = subject.title()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}"
    
first = ClassPeriod("Computer Programming 2", room = 200)
second = ClassPeriod("Computer Programming 2", room = 200)
third = ClassPeriod("Computer Science Principles", room = 200)
sixth = ClassPeriod("Computer Science Principles", room = 200)

print(first, second, third, sixth)
