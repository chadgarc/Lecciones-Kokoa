
# Modulos
import sys, pygame,time
from pygame.locals import *

# Constantes/ Dimensiones de ventana
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
speed = 20
posx = 200
posy = 300
FPS = 30
fpsClock = pygame.time.Clock()

def Nube():
    #(fondo de la ventana, color, posicion, radio, borde)
    # Nube 1 arriba
    pygame.draw.circle(screen, (255, 250, 250), (280, 150), 100, 0)
    pygame.draw.circle(screen, (255, 250, 250), (170, 175), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (200, 175), 80, 0)
    pygame.draw.circle(screen, (255, 250, 250), (390, 175), 60, 0)
    pygame.draw.circle(screen, (255, 250, 250), (415, 175), 50, 0)
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

    while True:

        keys_pressed = pygame.key.get_pressed()
        Nube()
        screen.blit(pygame.image.load("gohan.png"), (posx,posy))
        pygame.display.update()
        screen.fill((135,206,250))

      # Comprobacion de eventos
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit("QUIT")

        if keys_pressed[K_LEFT]:
            if (posx<=10):
                posx = 920
            else:
                posx -= 10
            print ("Left")

        if keys_pressed[K_RIGHT]:
            if (posx>=920):
                posx = 10
            else:
                posx += 10
                print ("Right")

        if keys_pressed[K_UP]:
            if (posy<=10):
                posy = 520
            else:
                posy -= 10
            print ("Left")

        if keys_pressed[K_DOWN]:
            if (posy>=520):
                posy = 10
            else:
                posy += 10
            print ("Left")

        pygame.time.delay(3)
        fpsClock.tick(FPS)
