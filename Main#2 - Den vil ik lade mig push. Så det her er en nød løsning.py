import pygame, sys, os, time
from pygame import mixer

#Pygame setup
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("PenguinGame")
pygame.init()
clock = pygame.time.Clock()

#Billeder
QuitGame = pygame.image.load("resources\images\Quit.png")
playagain = pygame.image.load("resources\images\PlayAgain.png")
Trees = pygame.image.load('resources\images\Trees1.png')
mBG = pygame.image.load('resources\images\Mountain.png')
Snowman = pygame.image.load('resources\images\Snowman001.png')
Foreground = pygame.image.load('resources\images\Foreground.png')
char = pygame.image.load("resources\images\char.png")
enemy = pygame.image.load("resources\images\Træstub.png")
controlsScreen = pygame.image.load("resources\images\Controls.png")
image1 = pygame.image.load('resources\images\rightpip1.png')
image2 = pygame.image.load('resources\images\rightpip2.png')
image3 = pygame.image.load('resources\images\rightpip3.png')
image4 = pygame.image.load('resources\images\rightpip4.png')
image5 = pygame.image.load('resources\images\rightpip5.png')
image6 = pygame.image.load('resources\images\rightpip6.png')
image7 = pygame.image.load('resources\images\jumpingpip1.png')
image8 = pygame.image.load('resources\images\jumpingpip2.png')
image9 = pygame.image.load('resources\images\jumpingpip3.png')
image10 = pygame.image.load('resources\images\jumpingpip4.png')
image11 = pygame.image.load('resources\images\jumpingpip5.png')
image12 = pygame.image.load('resources\images\deadpip1.png')
image13 = pygame.image.load('resources\images\deadpip2.png')
image14 = pygame.image.load('resources\images\deadpip3.png')
image15 = pygame.image.load('resources\images\deadpip4.png')
image16 = pygame.image.load('resources\images\deadpip5.png')
menuBG = [pygame.image.load('menu\BGAnimation\MainMenu1.png'),
          pygame.image.load('menu\BGAnimation\MainMenu2.png'),
          pygame.image.load('menu\BGAnimation\MainMenu3.png'),
          pygame.image.load('menu\BGAnimation\MainMenu4.png'),
          pygame.image.load('menu\BGAnimation\MainMenu5.png'),
          pygame.image.load('startScene\MainMenu6.png')]

Door1 = pygame.image.load('menu\DoorAnimation\Door1.png')
Door2 = pygame.image.load('menu\DoorAnimation\Door2.png')
Door3 = pygame.image.load('menu\DoorAnimation\Door3.png')

menuBG2 = pygame.image.load('menu\MenuMountain.png')
JumpPenguinText = pygame.image.load('menu\JumpPenguinText.png')
PlayText = pygame.image.load('menu\PlayText.png')
ControlsText = pygame.image.load('menu\ControlsText.png')
QuitText = pygame.image.load('menu\QuitText.png')
FlossingPingvinBilleder = [pygame.image.load('menu\FlossingPingvin\FlossingPingvin1.png'),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin2.png'),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin3.png'),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin4.png'),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin5.png'),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin6.png')]

#Pygame mixer
mixer.init()

class Menu:
    def __init__(self, Repeats, AntalBilleder1, ImageNRAnimation, ImageNRFlossPingvin, SceneTid):
        self.ImageNRAnimation = ImageNRAnimation
        self.ImageNRFlossPingvin = ImageNRFlossPingvin
        self.repeats = Repeats
        self.AntalBilleder1 = AntalBilleder1
        self.Tid = SceneTid

    def animation(self):
        if PlayStart == True: #Animation for baggrunden i menuen og startscenen
            mixer.music.load('resources\soundEffects\Furnace.mp3')
            if self.AntalBilleder1 < 30:
                clock.tick(30)
                mixer.music.play()
                if self.ImageNRAnimation > 4: #Resetter listen af billeder
                    self.ImageNRAnimation = 0
                win.blit(menuBG[self.ImageNRAnimation], (0, 0))
                self.ImageNRAnimation += 1 #Skifter vores baggrund i menuen så den bliver animeret
                self.AntalBilleder1 += 1
                win.blit(Door1, (0, 0))
            else:
                self.Tid == -60
                win.blit(menuBG[5], (0, 0))
                mixer.music.stop()
                self.Tid += 1
                print(self.Tid)
                if self.Tid <= 9:
                    win.blit(Door1, (0, 0))
                if self.Tid >= 10 and self.Tid <= 20:
                    win.blit(Door2, (0, 0))
                if self.Tid >= 10 and self.Tid <= 25:
                    win.blit(image1, (102, 170))
                if self.Tid >= 21:
                    win.blit(Door3, (0, 0))
                if self.Tid >= 26 and self.Tid <= 27:
                    win.blit(image1, (102, 165))
                if self.Tid >= 28 and self.Tid <= 29:
                    win.blit(image1, (102, 155))
                if self.Tid >= 30 and self.Tid <= 31:
                    win.blit(image1, (102, 170))
                if self.Tid >= 32 and self.Tid <= 33:
                    win.blit(image1, (102, 180))
                if self.Tid >= 34 and self.Tid <= 35:
                    win.blit(image1, (102, 190))
                if self.Tid >= 36 and self.Tid <= 37:
                    win.blit(image1, (102, 200))
                if self.Tid >= 38 and self.Tid <= 39:
                    win.blit(image1, (102, 210))


        else:
            if self.ImageNRAnimation > 4:
                self.ImageNRAnimation = 0
            win.blit(menuBG[self.ImageNRAnimation], (0, 0))
            self.ImageNRAnimation += 1

    def MountainBG(self):
        win.blit(menuBG2, (0, -150))

    def jumpPenguinText(self):
        win.blit(JumpPenguinText, (0, 0))

    def PlayText(self):
        win.blit(PlayText, (0, -50))

    def ControlsText(self):
        win.blit(ControlsText, (0, 70))

    def QuitText(self):
        win.blit(QuitText, (0, 190))

    def Door(self):
        Door = pygame.image.load('startScene\Door.png')
        win.blit(Door, (0, 0))

    def FlossingPingvin(self):
        if self.ImageNRFlossPingvin > 5: #Resetter listen af billeder
            self.ImageNRFlossPingvin = 0
        win.blit(FlossingPingvinBilleder[self.ImageNRFlossPingvin], (750, 250))
        self.ImageNRFlossPingvin += 1 #Skifter vores baggrund i menuen så den bliver animeret







class MovBGs:
    def __init__(self, treespeed, snowmanspeed, foregroundspeed):
        self.W = 1000
        self.treeSpeed = treespeed
        self.xtree = 0
        self.snowmanSpeed = snowmanspeed
        self.xsnowman = 0
        self.foregroundSpeed = foregroundspeed
        self.xforeground = 0

    def mountainBG(self):
        win.blit(mBG, (0, 0))

    def movingTrees(self):
        rel_x_Trees = self.xtree % Trees.get_rect().width
        win.blit(Trees, (rel_x_Trees - Trees.get_rect().width, 60))
        if rel_x_Trees < self.W:
            win.blit(Trees, (rel_x_Trees, 60))
        self.xtree -= self.treeSpeed
        self.treeSpeed += 0.01

    def movingSnowman(self):
        rel_x_Snowman = self.xsnowman % Snowman.get_rect().width
        win.blit(Snowman, (rel_x_Snowman - Snowman.get_rect().width, 220))
        if rel_x_Snowman < self.W:
            win.blit(Snowman, (rel_x_Snowman, 220))
        self.xsnowman -= self.snowmanSpeed
        self.snowmanSpeed += 0.01

    def movingForeground(self):
        rel_x_foreground = self.xforeground % Foreground.get_rect().width
        win.blit(Foreground, (rel_x_foreground - Foreground.get_rect().width, 380))
        if rel_x_foreground < self.W:
            win.blit(Foreground, (rel_x_foreground, 380))
        self.xforeground -= self.foregroundSpeed
        self.foregroundSpeed += 0.01


class PointSystem:
    def __init__(self, score, xPos):
        self.Score = score
        self.xPos = xPos

    def PointSystem_On_Screen(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        text = font.render("Score: " + str(self.Score), True, (0, 0, 0))
        if run == True:
            win.blit(text, [self.xPos, 50])
            self.Score += 1


class Player1:
    def __init__(self, x, y, heigth, width):
            self.x = x
            self.y = y
            self.width = width
            self.h = heigth
            self.Jump = False
            self.JumpCount = 7
            self.hitbox = (self.x + 55, self.y + 63, 40, 73)
            self.neg = 1

    def sprite(self, win):
        win.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 55, self.y + 63, 40, 73)

    def hit(self):
        self.x = 50
        self.y = 325
        font1 = pygame.font.SysFont("comicsans",100)
        text = font1.render("game over",1, (255,0,0))
        win.blit(quit, (400, 350))
        win.blit(text, (325, 120))
        win.blit(playagain, (350, 200))
        pygame.display.update()
        RunMouseButton = True
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if RunMouseButton:
                        if 400 + 173 > mx > 400 and 350 + 104 > my > 350:
                            pygame.quit()
                if EVENT.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if RunMouseButton:
                        if 350 + 300 > mx > 350 and 200 + 100 > my > 200:  # Her tjekkes om musen er inde i "Play again" hitboxen
                            pause = False
                            self.Jump = False
                            self.JumpCount = 7

    def Jumping(self):
        keys = pygame.key.get_pressed()
        if not man.Jump:
            if keys[pygame.K_UP]:
                man.Jump = True
        else:
            if man.JumpCount >= -7:
                neg = 1
                if man.JumpCount <= 0:
                    neg = -1
                man.y -= (man.JumpCount ** 2) * 0.5 * neg
                man.JumpCount -= 1
            else:
                man.Jump = False
                man.JumpCount = 7


class Enemy:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.vel = 10
        self.hitbox = (self.x + 35, self.y + 13, 50, 80)

    def draw(self, win):
        win.blit(enemy, (self.x, self.y))
        self.hitbox = (self.x + 35, self.y + 13, 50, 80)

    def move(self):
        self.x -= self.vel
        if self.x < 0 - self.width:
            self.x = 1000
            self.vel += 1
    def hit(self):
        self.x = 1000
        self.y = 375

def RedrawGameWindow():
    if StopDrawing == False:
        if startspil == True:
            clock.tick(60)
            movBGs.mountainBG()
            movBGs.movingTrees()
            movBGs.movingForeground()
            movBGs.movingSnowman()
            pointSystem.PointSystem_On_Screen()
            man.sprite(win)
            obstacle.draw(win)
            obstacle.move()
            Player1.Jumping(0)
        else:
            if PlayStart == True: #Resten af startscenen placeres herinde og laver en cutscene
                Menu.MountainBG()
                Menu.animation()
                Menu.FlossingPingvin()
            elif ControlsStart == True:
                Menu.MountainBG()
                Menu.animation()
                Menu.FlossingPingvin()
                Menu.Door()
                win.blit(controlsScreen, (0, 0))
            elif QuitStart == True:
                quit()
            else:
                clock.tick(5)
                Menu.MountainBG()
                Menu.animation()
                Menu.jumpPenguinText()
                Menu.FlossingPingvin()
                Menu.Door()
                Menu.PlayText()
                Menu.ControlsText()
                Menu.QuitText()


class Buttons:
    mx, my = pygame.mouse.get_pos()

    def __init__(self):
        pass

    def PlayButton(self):
        global RunMouseButton
        global RunMouseButton2
        global PlayStart
        print(mx, my)
        if RunMouseButton == True and RunMouseButton2 == True:
            if 413 + 180 > mx > 413 and 158 + 80 > my > 158:  # Her tjekkes om musen er inde i "Play" hitboxen
                PlayStart = True
                RunMouseButton = False
                RunMouseButton2 = False

    def ControlsButton(self):
        global RunMouseButton
        global RunMouseButton2
        global ControlsStart
        if RunMouseButton == True and RunMouseButton2 == True:
            if 320 + 357 > mx > 320 and 285 + 80 > my > 285:  # Her tjekkes om musen er inde i "Controls" hitbox # todo mangler en baggrund og en knap der fører tilbage til main menu
                win.fill((255, 0, 0))
                ControlsStart = True
                RunMouseButton2 = False
        if ControlsStart == True and RunMouseButton2 == False:
            if 432 + 133 > mx > 432 and 368 + 42 > my > 368:
                ControlsStart = False
                RunMouseButton2 = True

    def QuitButton(self):
        global RunMouseButton
        global RunMouseButton2
        global QuitStart
        if RunMouseButton == True and RunMouseButton2 == True:
            if 423 + 147 > mx > 423 and 400 + 80 > my > 400:  # Her tjekkes om musen er inde i "Quit" hitbox # todo mangler en baggrund
                win.fill((0, 255, 0))
                RunMouseButton = False
                RunMouseButton2 = False
                QuitStart = True

man = Player1(50, 375, 50, 50)
obstacle = Enemy(1000, 395, 50, 50)
movBGs = MovBGs(3, 10, 10)
pointSystem = PointSystem(0, 400)
Menu = Menu(3, 0, 0, 0, 0)
buttons = Buttons()


# todo Skal flyttes senere
PlayStart = False
startspil = False #Bliver ikke brugt pt, men det sætter selve spillet igang
StopDrawing = False
ControlsStart = False
QuitStart = False
RunMouseButton = True  # Gør så man ikke kan trykke på knapperne efter de bliver fjernet
RunMouseButton2 = True
run = True
while run:
    if man.hitbox[1] < obstacle.hitbox[1] + obstacle.hitbox[3] and man.hitbox[1] + man.hitbox[3] > obstacle.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > obstacle.hitbox[0] and man.hitbox[0] < obstacle.hitbox[0] + obstacle.hitbox[2]:
            man.hit()
            obstacle.hit()
            pointSystem = PointSystem(0, 400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            buttons.PlayButton()
            buttons.ControlsButton()
            buttons.QuitButton()

    RedrawGameWindow()
    pygame.display.update()

pygame.QUIT

#test test this is test