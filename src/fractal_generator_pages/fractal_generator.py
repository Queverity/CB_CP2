# CB 1st Fractal Generator
# Note: turtle2img needs to be pip downloaded

import turtle
import turtle2img

# define function intialize_turtle()

# define function draw_sierpinski(fractal_depth,fractal_color):
    # so the basics of a sierpinski triangle is drawing a triangle inside another triangle, where the vertexes are on the midpoints of the first triangle, and the sides are half the length of the first triangle
    # base case: fractal depth equals set fractal depth

# define function image_saver():
    # use turtle2img to save the image as a png file


# define function main_menu():
    # introduce program

    # ask user whether they would like to generate a sierpinski triangle or a koch snowflake

    # ask user for fractal depth

    # ask user for background color and fractal color

    # run fractal generator based on the fractal depth and color inputs

    # ask user if they would like to save it as an image

    # ask user if they would like to continue using the program


def draw_triangle(distance,illustrator):
    for _ in range(3):
        illustrator.forward(distance)
        illustrator.left(120)

def draw_sierpinski(depth, distance,illustrator):
    if depth == 0:
        draw_triangle(distance,illustrator)
    else:
        draw_sierpinski(depth-1, distance/2,illustrator)

        illustrator.forward(distance/2)
        draw_sierpinski(depth-1, distance/2,illustrator)
        illustrator.backward(distance/2)

        illustrator.left(60)
        illustrator.forward(distance/2)
        illustrator.right(60)

        draw_sierpinski(depth-1, distance/2,illustrator)

        illustrator.left(60)
        illustrator.backward(distance/2)
        illustrator.right(60)


def intilialize_turtle(background_color,turtle_color):
    wn = turtle.Screen()
    wn.bgcolor(background_color)
    wn.title("Triangle")

    illustrator = turtle.Turtle()
    illustrator.turtlesize(3,3)
    illustrator.color(turtle_color)
    illustrator.speed(0) 
    illustrator.width(3)
    illustrator.teleport(-600,-475)

    return illustrator

def image_saver(file_name):
    turtle2img.save_png(file_name)

def main():
    print("This is a Sierpinski Triangle Fractal Generator!")
    print("It will generate a triangle based on the fractal depth, color, and background color you set.")
    while True:
        fractal_depth = int(input("Please enter the fractal depth (1-6): "))
        if fractal_depth < 1 or fractal_depth > 6:
            print("Fractal depth must be between 1 and 6. Please try again.")
            continue
        background_color = input("Please enter the background color: ")
        turtle_color = input("Please enter the fractal color: ")
        try:
            illustrator = intilialize_turtle(background_color,turtle_color)
            draw_sierpinski(fractal_depth, 1200, illustrator)
        except:
            print("You have entered an invalid color. Please try again.")
            continue
        else:
            save_image = input("Would you like to save the image as a png file? (y/n):\n").strip()
            if save_image.lower() == "y":
                file_name = input("Please enter the file name (without extension):\n").strip()
                image_saver(file_name + ".png")
            continue_program = input("Would you like to generate another fractal? (y/n):\n").strip()
            if continue_program.lower() == "n":
                print("Goodbye!")
                break

main()

