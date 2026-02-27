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