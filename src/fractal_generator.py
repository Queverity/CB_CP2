# CB 1st Fractal Generator
# Note: turtle2img needs to be downloaded

import turtle

# define function intialize_turtle()

# define function draw_sierpinski(fractal_depth,fractal_color):
    # so the basics of a sierpinski triangle is drawing a triangle inside another triangle, where the vertexes are on the midpoints of the first triangle, and the sides are half the length of the first triangle
    # base case: fractal depth equals set fractal depth

def draw_sierpinski(current_fractal_depth,set_fractal_depth):
    if current_fractal_depth > set_fractal_depth: return
    current_fractal_depth += 1
    
        
    for i in range(1,6):
        distance = 1200/2**set_fractal_depth
        set_fractal_depth -= 1
        
        illustrator.teleport(-600,-525)
        def draw_triangle(distance):
            illustrator.forward(distance)
            illustrator.left(120)
            illustrator.forward(distance)
            illustrator.left(120)
            illustrator.forward(distance)
            illustrator.left(120)
        
        count = 0
        for _ in range(1,4):
                if count == 2:
                    count = 0 
                    illustrator.backward(distance*4)
                    illustrator.left(60)
                    illustrator.forward(distance*2)
                    illustrator.right(60)
                    # This is only to draw the very top triangle
                    draw_triangle(distance)
                    illustrator.forward(distance)
                    draw_triangle(distance)
                    illustrator.backward(distance)
                    illustrator.left(60)
                    illustrator.forward(distance)
                    illustrator.right(60)
                    draw_triangle(distance)
                    illustrator.left(60)
                    illustrator.backward(distance)
                    illustrator.right(60)
                    illustrator.forward(distance*2)
                else:
                    count += 1
                    draw_triangle(distance)
                    illustrator.forward(distance)
                    draw_triangle(distance)
                    illustrator.backward(distance)
                    illustrator.left(60)
                    illustrator.forward(distance)
                    illustrator.right(60)
                    draw_triangle(distance)
                    illustrator.left(60)
                    illustrator.backward(distance)
                    illustrator.right(60)
                    illustrator.forward(distance*2)
                    
    return draw_sierpinski(current_fractal_depth,set_fractal_depth)


wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Triangle")

illustrator = turtle.Turtle()
illustrator.turtlesize(3,3)
illustrator.color("yellow")
illustrator.speed(0) 
illustrator.width(3)

set_fractal_depth = 5

draw_sierpinski(-3,5)


turtle.done()


# define function draw_koch(fractal_depth,fractal_color):

# define function image_saver():

# define function main_menu():
    # introduce program

    # ask user whether they would like to generate a sierpinski triangle or a koch snowflake

    # ask user for fractal depth

    # ask user for background color and fractal color

    # run fractal generator based on the fractal depth and color inputs

    # ask user if they would like to save it as an image

    # ask user if they would like to continue using the program