import pygame
import os


class Player:
    x=0
    y=0
    xSpeed=5
    ySpeed=5
    maxSpeed=5
    width=20
    height=20
    color=(0,149,243)
    points=0
    theScreen=0


    def __init__(self,xpos,ypos,screen):
        self.x=xpos
        self.y=ypos
        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0]
        self.screenHeight = self.theScreen.get_size()[1]

    def draw(self):
        pass

    def update(self):
        self.x=self.x + self.xSpeed
        self.y=self.y + self.ySpeed

image1 = pygame.image.load('images/1.png')
image2 = pygame.image.load('images/2.png')
image3 = pygame.image.load('images/3.png')
image4 = pygame.image.load('images/4.png')
image5 = pygame.image.load('images/5.png')
image6 = pygame.image.load('images/6.png')
image7 = pygame.image.load('images/jumpingpip1.png')
image8 = pygame.image.load('images/jumpingpip2.png')
image9 = pygame.image.load('images/jumpingpip3.png')
image10 = pygame.image.load('images/jumpingpip4.png')
image11 = pygame.image.load('images/jumpingpip5.png')
image12 = pygame.image.load('images/deadpip1.png')
image13 = pygame.image.load('images/deadpip2.png')
image14 = pygame.image.load('images/deadpip3.png')
image15 = pygame.image.load('images/deadpip4.png')


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

pip = Player(10,screen.get_size()[1]-50,screen)

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done == True

    #update
    pip.update()

    #draw
    screen.fill((0, 0, 0))
    pip.draw()


    screen.blit(image1, (0,0))
    pygame.display.update()