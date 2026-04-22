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

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

class ColoredRect:
    def __init__(self,x,y,w,h,color):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
    
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)
    
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h,color,on_ground):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,w,h)
        self.speed = 5
        self.color = color
        self.on_ground = on_ground

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
        elif keys[pygame.K_SPACE] and self.on_ground == True:
            self.y -= vel_y
            
            self.on_ground = False

            self.rect.y = self.y

            if self.y > 480:
                self.y == 480
                self.on_ground = True

        else:
            pass

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect)

    def update(self,surface):
        self.get_input()
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw(surface)


    


player = Player(400,400,25,25,RED,on_ground)
block = ColoredRect(300,300,50,50,BLUE)

# infinite loop 
while run: 
    pygame.time.Clock().tick(60)

    old_x, old_y = x, y

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    
    win.fill(WHITE)

    
    block.draw(win)
    player.update(win)

    
    pygame.display.update() 
