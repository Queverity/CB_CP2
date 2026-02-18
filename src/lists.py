# VL 1st Types of Lists Notes

# Lists
siblings = ["Rosie","Andy","Anthony","Viola","Evalyn","Wren","Morgan"]

print(siblings[3])
siblings[-1] = "DOW"

print(siblings)


# Tuples
fruit = ("apple", "orange", "peach", "kiwi", "raspberry")

home = (0,0)


# This is unpacking a tuple, where you assign variables to the values in a tuple.
x,y = home

print(x)

print(y)


# Sets
colors = {"Orange", "Purple", "Green", "Blue", "Yellow", "Red"}
colors.add("Pink")
colors.remove("Purple")

print(colors)

for i in colors:
    if i == "Orange":
        i = "Burgundy"
        print(i)
    else:
        print(i)

