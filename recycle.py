import pygame
import random
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

    pygame.display.update()


 