# CB 1st Function Decomposition Notes

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World")

greet()

@decorator
def add():
    print(1+1)

add()