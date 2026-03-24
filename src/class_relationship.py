# CB 1st Class Relationship Notes

# Parent Class

# Inheritance "is a"

class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford","Mustang")

boat = Boat("Ibiza", "Touring 20")

plane = Plane("Boeing", "747")

car.move()
boat.move()
plane.move()

# Aggregation "has a"

class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        try:
            self.catalog.pop(book)
        except:
            print("Book name is wrong or book is not in library")
        else:
            print("Book succesfully removed")

    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title} by {self.author}"
    
lib = Library("Provo Library")

lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Fellowship of the Rink", "J. R. R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S Lewis"))

lib.view_catalog()

# Composition