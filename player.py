import pygame, sys, os, time

#Pygame setup
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("PenguinGame")
pygame.init()
clock = pygame.time.Clock()

#Billeder
Trees = pygame.image.load('resources\images\Trees1.png')
mBG = pygame.image.load('resources\images\Mountain.png')
Snowman = pygame.image.load('resources\images\Snowman001.png')
Foreground = pygame.image.load('resources\images\Foreground.png')
char = pygame.image.load("resources\images\L1.png")
enemy = pygame.image.load("resources\images\L1E.png")

class Sound:
    def __init__(self):
        pass
    def Music1(self):
        pygame.mixer.music.load('audio/Song1.mp3')
        #pygame.mixer.music.play()

    def Music2(self):
        pygame.mixer.music.load('audio/CookingByTheBook.mp3')
        #pygame.mixer.music.play()

class Menu:
    def __init__(self, Repeats, AntalBilleder1, ImageNRAnimation, ImageNRFlossPingvin):
        self.ImageNRAnimation = ImageNRAnimation
        self.ImageNRFlossPingvin = ImageNRFlossPingvin
        self.repeats = Repeats
        self.AntalBilleder1 = AntalBilleder1

    def animation(self):
        menuBG = [pygame.image.load('menu\BGAnimation\MainMenu1.png'),
                  pygame.image.load('menu\BGAnimation\MainMenu2.png'),
                  pygame.image.load('menu\BGAnimation\MainMenu3.png'),
                  pygame.image.load('menu\BGAnimation\MainMenu4.png'),
                  pygame.image.load('menu\BGAnimation\MainMenu5.png'),
                  pygame.image.load('startScene\MainMenu6.png')]
        if PlayStart == True: #Animation for baggrunden i menuen og startscenen
            if self.AntalBilleder1 < 10:
                if self.ImageNRAnimation > 4: #Resetter listen af billeder
                    self.ImageNRAnimation = 0
                win.blit(menuBG[self.ImageNRAnimation], (0, 0))
                self.ImageNRAnimation += 1 #Skifter vores baggrund i menuen så den bliver animeret
                self.AntalBilleder1 += 1
            else:
                win.blit(menuBG[5], (0, 0))
        else:
            if self.ImageNRAnimation > 4:
                self.ImageNRAnimation = 0
            win.blit(menuBG[self.ImageNRAnimation], (0, 0))
            self.ImageNRAnimation += 1

    def MountainBG(self):
        menuBG2 = pygame.image.load('menu\MenuMountain.png')
        win.blit(menuBG2, (0, -150))

    def jumpPenguinText(self):
        JumpPenguinText = pygame.image.load('menu\JumpPenguinText.png')
        win.blit(JumpPenguinText, (0, 0))

    def PlayText(self):
        PlayText = pygame.image.load('menu\PlayText.png')
        win.blit(PlayText, (0, -50))

    def ControlsText(self):
        ControlsText = pygame.image.load('menu\ControlsText.png')
        win.blit(ControlsText, (0, 70))

    def QuitText(self):
        QuitText = pygame.image.load('menu\QuitText.png')
        win.blit(QuitText, (0, 190))

    def Door(self):
        Door = pygame.image.load('startScene\Door.png')
        win.blit(Door, (0, 0))

    def FlossingPingvin(self):
        FlossingPingvinBilleder = [pygame.image.load('menu\FlossingPingvin\FlossingPingvin1.png'), pygame.image.load('menu\FlossingPingvin\FlossingPingvin2.png'), pygame.image.load('menu\FlossingPingvin\FlossingPingvin3.png'), pygame.image.load('menu\FlossingPingvin\FlossingPingvin4.png'), pygame.image.load('menu\FlossingPingvin\FlossingPingvin5.png'), pygame.image.load('menu\FlossingPingvin\FlossingPingvin6.png')]
        if self.ImageNRFlossPingvin > 5: #Resetter listen af billeder
            self.ImageNRFlossPingvin = 0
        win.blit(FlossingPingvinBilleder[self.ImageNRFlossPingvin], (750, 250))
        self.ImageNRFlossPingvin += 1 #Skifter vores baggrund i menuen så den bliver animeret


class StartScene:
    def __init__(self):
        pass
    def polarBearAnimation(self):
        pass


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
            #self.hitbox = (self.x + 20, self.y, 28, 60)


    def sprite(self,win):
        win.blit(char, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)

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
        self.vel = 5
        self.hitbox = (self.x + 20, self.y, 28, 60)
    def draw(self,win):
        win.blit(enemy, (self.x, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        self.x -= self.vel
        if self.x == 0 -self.width:
            self.x = 1000
            #self.vel = self.vel + 1



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
                clock.tick(3)
                Menu.MountainBG()
                Menu.animation()
                Menu.FlossingPingvin()
                Menu.Door()
                startScene.polarBearAnimation()
            elif ControlsStart == True:
                win.fill((255, 0, 0))
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

man = Player1(50, 400, 50, 50)
obstacle = Enemy(1000, 400, 50, 50)
movBGs = MovBGs(3, 10, 10)
pointSystem = PointSystem(0, 400)
Menu = Menu(3, 0, 0, 0)
Sound = Sound()
startScene = StartScene()

# todo Skal flyttes senere
PlayStart = False
startspil = False
StopDrawing = False
ControlsStart = False
QuitStart = False
RunMouseButton = True #Gør så man ikke kan trykke på knapperne efter de bliver fjernet

Sound.Music2()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if RunMouseButton == True:
                if 413 + 180 > mx > 413 and 158 + 80 > my > 158:  # Her tjekkes om musen er inde i "Play" hitboxen
                    PlayStart = True
                    RunMouseButton = False
                elif 320 + 357 > mx > 320 and 285 + 80 > my > 285:  # Her tjekkes om musen er inde i "Controls" hitbox # todo mangler en baggrund
                    win.fill((255, 0, 0))
                    RunMouseButton = False
                    ControlsStart = True
                elif 423 + 147 > mx > 423 and 400 + 80 > my > 400:  # Her tjekkes om musen er inde i "Quit" hitbox # todo mangler en baggrund
                    win.fill((0, 255, 0))
                    RunMouseButton = False
                    QuitStart = True

    RedrawGameWindow()
    pygame.display.update()

pygame.QUIT

#Test 3