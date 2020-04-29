import pygame, sys, os, time
from pygame import mixer

#Pygame setup
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("PenguinGame")
pygame.init()
clock = pygame.time.Clock()

#Billeder
playagain = pygame.image.load("resources\images\PlayAgain.png").convert_alpha()
Trees = pygame.image.load('resources\images\Trees1.gif').convert_alpha()
mBG = pygame.image.load('resources\images\Mountain.png').convert_alpha()
Snowman = pygame.image.load('resources\images\Snowman001.png').convert_alpha()
Foreground = pygame.image.load('resources\images\Foreground.gif').convert_alpha()
char = pygame.image.load("resources\images\char.png").convert_alpha()
enemy = pygame.image.load("resources\images\L1.png").convert_alpha()
controlsScreen = pygame.image.load("resources\images\Controls.png").convert_alpha()
image1 = pygame.image.load('resources\images\Rightpip1.png')
image2 = pygame.image.load('resources\images\Rightpip2.png')
image3 = pygame.image.load('resources\images\Rightpip3.png')
image4 = pygame.image.load('resources\images\Rightpip4.png')
image5 = pygame.image.load('resources\images\Rightpip5.png')
image6 = pygame.image.load('resources\images\Rightpip6.png')
image7 = pygame.image.load('resources\images\Jumpingpip1.png')
image8 = pygame.image.load('resources\images\Jumpingpip2.png')
image9 = pygame.image.load('resources\images\Jumpingpip3.png')
image10 = pygame.image.load('resources\images\Jumpingpip4.png')
image11 = pygame.image.load('resources\images\Jumpingpip5.png')
image12 = pygame.image.load('resources\images\deadpip1.png')
image13 = pygame.image.load('resources\images\deadpip2.png')
image14 = pygame.image.load('resources\images\deadpip3.png')
image15 = pygame.image.load('resources\images\deadpip4.png')
image16 = pygame.image.load('resources\images\deadpip5.png')
image17 = pygame.image.load('resources\images\Animationpip1.png')
ExclamationMark = pygame.image.load('resources\images\ExclamationMark.png')
QuestionMark = pygame.image.load('resources\images\QuestionMark.png')
menuBG = [pygame.image.load('menu\BGAnimation\MainMenu1.png'),
          pygame.image.load('menu\BGAnimation\MainMenu2.png'),
          pygame.image.load('menu\BGAnimation\MainMenu3.png'),
          pygame.image.load('menu\BGAnimation\MainMenu4.png'),
          pygame.image.load('menu\BGAnimation\MainMenu5.png'),
          pygame.image.load('startScene\MainMenu6.png')]
WalkingPip = [image12, image13, image14]


Door1 = pygame.image.load('menu\DoorAnimation\Door1.png').convert_alpha()
Door2 = pygame.image.load('menu\DoorAnimation\Door2.png').convert_alpha()
Door3 = pygame.image.load('menu\DoorAnimation\Door3.png').convert_alpha()
menuBG2 = pygame.image.load('menu\MenuMountain.png').convert_alpha()
JumpPenguinText = pygame.image.load('menu\JumpPenguinText.png').convert_alpha()
PlayText = pygame.image.load('menu\PlayText.png').convert_alpha()
ControlsText = pygame.image.load('menu\ControlsText.png').convert_alpha()
QuitText = pygame.image.load('menu\QuitText.png').convert_alpha()
FlossingPingvinBilleder = [pygame.image.load('menu\FlossingPingvin\FlossingPingvin1.png').convert_alpha(),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin2.png').convert_alpha(),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin3.png').convert_alpha(),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin4.png').convert_alpha(),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin5.png').convert_alpha(),
                           pygame.image.load('menu\FlossingPingvin\FlossingPingvin6.png').convert_alpha()]
#Pygame mixer
mixer.init()
mixer.music.load('resources\soundEffects\Furnace.mp3')

class Menu:
    def __init__(self, Repeats, AntalBilleder1, ImageNRAnimation, ImageNRFlossPingvin, SceneTid, xPosAnimation, yPosAnimation, WalkingAnimation):
        self.ImageNRAnimation = ImageNRAnimation
        self.ImageNRFlossPingvin = ImageNRFlossPingvin
        self.repeats = Repeats
        self.AntalBilleder1 = AntalBilleder1
        self.Tid = SceneTid
        self.xPos = xPosAnimation
        self.yPos = yPosAnimation
        self.WalkingAnimation = WalkingAnimation

    def animation(self):

        if PlayStart == True: #Animation for baggrunden i menuen og startscenen. Ikke færdig endnu men in progress
            global startspil
            if self.AntalBilleder1 < 30:
                clock.tick(5)
                mixer.music.play()
                if self.ImageNRAnimation > 4: #Resetter listen af billeder
                    self.ImageNRAnimation = 0
                win.blit(menuBG[self.ImageNRAnimation], (0, 0))
                self.ImageNRAnimation += 1 #Skifter vores baggrund i menuen så den bliver animeret
                self.AntalBilleder1 += 1
                win.blit(Door1, (0, 0))
            else:
                clock.tick(20)
                win.blit(menuBG[5], (0, 0))
                mixer.music.stop()
                print(self.Tid)
                self.Tid += 1
                if self.Tid <= 15:
                    win.blit(Door1, (0, 0))

                elif self.Tid >= 16 and self.Tid <= 25:
                    win.blit(Door2, (0, 0))

                elif self.Tid >= 22 and self.Tid <= 30:
                    win.blit(Door3, (0, 0))

                elif self.Tid >= 30 and self.Tid <= 37:
                    win.blit(Door2, (0, 0))

                elif self.Tid >= 37:
                    win.blit(Door1, (0, 0))

                if self.Tid >= 16 and self.Tid <= 60:
                    win.blit(image1, (self.xPos, self.yPos))

                elif self.Tid >= 60 and self.Tid <= 63:
                    win.blit(image17, (self.xPos, self.yPos))
                    self.yPos -= 5
                    print(self.xPos, self.yPos)

                elif self.Tid >= 63 and self.Tid <= 70:
                    win.blit(image17, (self.xPos, self.yPos))
                    self.yPos += 10
                    print(self.xPos, self.yPos)

                elif self.Tid >= 70 and self.Tid <= 170:
                    win.blit(QuestionMark, (0, 0))
                    if self.WalkingAnimation > 2:  # Resetter listen af billeder
                        self.WalkingAnimation = 0
                    win.blit(WalkingPip[self.WalkingAnimation], (self.xPos, self.yPos))
                    self.WalkingAnimation += 1  # Skifter vores baggrund i menuen så den bliver animeret
                    if self.xPos <= 700:
                        self.xPos += 7.5

                elif self.Tid == 200:
                    startspil = True





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
        win.blit(Door1, (0, 0))

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
        win.blit(Trees, (rel_x_Trees - Trees.get_rect().width, 0))
        if rel_x_Trees < self.W:
            win.blit(Trees, (rel_x_Trees, 0))
        self.xtree -= self.treeSpeed
        self.treeSpeed += 0.01

    def movingSnowman(self):
        rel_x_Snowman = self.xsnowman % Snowman.get_rect().width
        win.blit(Snowman, (rel_x_Snowman - Snowman.get_rect().width, 170))
        if rel_x_Snowman < self.W:
            win.blit(Snowman, (rel_x_Snowman, 170))
        self.xsnowman -= self.snowmanSpeed
        self.snowmanSpeed += 0.01

    def movingForeground(self):
        rel_x_foreground = self.xforeground % Foreground.get_rect().width
        win.blit(Foreground, (rel_x_foreground - Foreground.get_rect().width, 0))
        if rel_x_foreground < self.W:
            win.blit(Foreground, (rel_x_foreground, 0))
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
            self.hitbox = (self.x + 25, self.y + 29, 50, 56)
            self.neg = 1


    def sprite(self,win):
        win.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 25, self.y + 29, 50, 56)

    def hit(self):
        self.x = 60
        self.y = 375
        font1 = pygame.font.SysFont("comicsans",100)
        text = font1.render("game over",1, (255,0,0))
        win.blit(text, (325, 120))
        win.blit(playagain, (400, 250))
        pygame.display.update()
        RunMouseButton = True
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if RunMouseButton == True:
                        if 400 + 200 > mx > 400 and 250 + 66 > my > 250:  # Her tjekkes om musen er inde i "Play again" hitboxen
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    def draw(self,win):
        win.blit(enemy, (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def move(self):
        self.x -= self.vel
        if self.x < 0 - self.width:
            self.x = 1000
            self.vel += 1
    def hit(self):
        self.x = 1000
        self.y = 395


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
            elif ControlsStart == True:
                clock.tick(5)
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
Menu = Menu(3, 0, 0, 0, 0, 102, 170, 0)
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
