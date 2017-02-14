
# Modulos
import sys, pygame, time
from pygame.locals import *

# Constantes/ Dimensiones de ventana
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
speed = 11
FPS=30
fpsClock=pygame.time.Clock()

# Circulo
def Nube():
    #(fondo de la ventana, color, posicion, radio, borde)
    # Nube 1 arriba
    pygame.draw.circle(screen, (255, 250, 250), (350, 150), 100, 0)
    pygame.draw.circle(screen, (255, 250, 250), (240, 175), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (270, 175), 80, 0)
    pygame.draw.circle(screen, (255, 250, 250), (460, 175), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (485, 175), 50, 0)
    # Nube 2 abajo
    pygame.draw.circle(screen, (255, 250, 250), (650, 450), 100, 0)
    pygame.draw.circle(screen, (255, 250, 250), (540, 475), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (570, 475), 80, 0)
    pygame.draw.circle(screen, (255, 250, 250), (760, 475), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (785, 475), 50, 0)

# Funciones
def main():
    pygame.display.set_caption("Gohan Volando")
    return 0


if __name__ == '__main__':
    pygame.init()
    main()

class gohan(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gohan.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 100
        self.rect.centery = height /2

gohan = gohan(30)

while True:
    key = pygame.key.get_pressed()
    Nube()
    screen.blit(gohan.image, gohan.rect)
    pygame.display.update()
    screen.fill((135,206,250))
    # Comprobacion de eventos
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()

    if key[K_LEFT]:
        if (gohan.rect.left<=10):
            gohan.rect.left = 920
        else:
            gohan.rect.left -= speed
            print ("Left")

    if key[K_RIGHT]:
        if (gohan.rect.right>=920):
            gohan.rect.right = 70
        else:
            gohan.rect.right += speed
            print ("Right")

    if key[K_UP]:
        if (gohan.rect.top<=10):
            gohan.rect.top = 520
        else:
            gohan.rect.top -= speed
            print ("Up")

    if key[K_DOWN]:
        if (gohan.rect.bottom>=600):
            gohan.rect.bottom = 70
        else:
            gohan.rect.bottom += speed
            print ("Down")

    pygame.time.delay(10)
    fpsClock.tick(FPS)
