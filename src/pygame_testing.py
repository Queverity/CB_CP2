import pygame

pygame.init()

win = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Moving rectangle") 

x = 200
y = 480

width = 20
height = 20

vel_x = 10
vel_y = 5
run = True

on_ground = True
gravity = 0.8

# infinite loop 
while run: 
    pygame.time.Clock().tick(60)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT] and x>0: 
        x -= vel_x

    if keys[pygame.K_RIGHT] and x<500-width: 
        x += vel_x 

    if keys[pygame.K_SPACE] and on_ground == True:
        on_ground = False
        vel_y -= 15


    if not on_ground:
        y += vel_y
        vel_y += gravity

        if y >= 480:
            y = 480
            on_ground = True
            vel_y = 0

    win.fill((255,255,255)) 
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 
    pygame.draw.rect(win,(0,255,0),(400,400,100,100))
    pygame.display.update() 
