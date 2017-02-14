
# Modulos
import sys, pygame, time
from pygame.locals import *

# Constantes/ Dimensiones de ventana
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
SPEED = 12
POSX = 100
POSY = 300
FPSCLOCK = pygame.time.Clock()
FPS = 30

# Funciones
def main():
    pygame.display.set_caption("Gohan")
    return 0

if __name__ == '__main__':
    pygame.init()
    main()

    while True:
        SCREEN.fill((135,206,250))
        GOHAN = pygame.image.load("gohan.png")
        SCREEN.blit(GOHAN, (POSX,POSY))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        # Comprobacion de eventos
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        if keys[K_LEFT]:
            if (POSX<=10):
                POSX = 10
            else:
                POSX -= SPEED
                print ("Left")

        if keys[K_RIGHT]:
            if (POSX>=920):
                POSX = 920
            else:
                POSX += SPEED
                print ("Right")

        if keys[K_UP]:
            if (POSY<=10):
                POSY = 10
            else:
                POSY -= SPEED
                print ("Up")

        if keys[K_DOWN]:
            if (POSY>=520):
                POSY = 520
            else:
                POSY += SPEED
                print ("Down")

        pygame.time.delay(3)
        FPSCLOCK.tick(FPS)
