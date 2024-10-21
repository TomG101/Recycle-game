import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 900
TITLE = "Recycle"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
run = True
binbin = pygame.image.load("bin.png")
pencil = pygame.image.load("pencil.png")
paper_bag = pygame.image.load("paper bag.png")
bg = pygame.image.load("bg earth.png")
box = pygame.image.load("box.png")
plastic_bag = pygame.image.load("plastic bag.png")
score = 0

class Recycle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.images = [pencil,paper_bag,box]
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Non_recycle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = plastic_bag
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(). __init__()
        self.image = pygame.transform.scale(binbin,(70,100))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

bin_group = pygame.sprite.Group()
recycle_group = pygame.sprite.Group()
non_recycle_group = pygame.sprite.Group()

bin = Bin(50,50)
bin_group.add(bin)

for i in range(30):
    x = random.randint(50,950)
    y = random.randint(50,850)
    recycle = Recycle(x,y)
    recycle_group.add(recycle)
for i in range(30):
    x = random.randint(50,950)
    y = random.randint(50,850)
    non_recycle = Non_recycle(x,y)
    non_recycle_group.add(non_recycle)





    
while run == True:
    screen.blit(bg,(0,0))
    bin_group.draw(screen)
    recycle_group.draw(screen)
    non_recycle_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        bin.rect.y -= 1
    if keys_pressed[pygame.K_DOWN]:
        bin.rect.y += 1
    if keys_pressed[pygame.K_LEFT]:
        bin.rect.x -= 1
    if keys_pressed[pygame.K_RIGHT]:
        bin.rect.x += 1

    if pygame.sprite.groupcollide(bin_group,recycle_group,False,True):
        score += 1
    if pygame.sprite.groupcollide(bin_group,non_recycle_group,False,True):
        score -= 1

    font = pygame.font.SysFont("calibri",50)
    text = font.render("Score:  "+ str(score),True,"black")
    screen.blit(text,(10,10))
    if len(recycle_group) == 0:
        run = False
        font = pygame.font.SysFont("calibri",20)
        text = font.render("GAME OVER! YOUR SCORE WAS: "+ str(score),True,"red")
        screen.blit(text,(100,350))
        pygame.display.update()
        pygame.time.delay(5000)

    
    

    pygame.display.update()


 