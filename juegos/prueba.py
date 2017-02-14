
############################### Modulos ###############################
import pygame, sys

################## Constantes/ Dimensiones de ventana #################
width = 1200
height = 600
screen = pygame.display.set_mode((width,height))

############################## Funciones ##############################
def main():
    pygame.display.set_caption("HOLA SOY UNA VENTANA, MIRA MIS FIGURAS :3")
    return 0

if __name__ == '__main__':
    pygame.init()
    main()

############################### Figuras ###############################

# Circulo
def pintarCirculo():
    #(fondo de la ventana, color, posicion, radio, borde)
    pygame.draw.circle(screen, (46, 139, 87), (900, 150), 110, 0)

# Cuadrado
    #(fondo de la ventana, color,(coordenadas(x,-y)) , dimendiones(ancho,altura), bordes)
def pintarCuadrado():
    pygame.draw.rect(screen, (25, 25, 112), pygame.Rect((180,55),(300,200)), 0)

# Estrella
puntos1 = [(400, 450), (600, 260), (800, 450)]
puntos2 = [(400, 320), (600, 520), (800, 320)]
def star():
    pygame.draw.polygon(screen, (178, 34, 34),puntos1 , 0)
    pygame.draw.polygon(screen, (178, 34, 34),puntos2 , 0)

# Ejecucion
while True:

    # Comprobacion de eventos
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            sys.exit()

    #Repintar de negro el fondo en cada ciclo
    screen.fill((0,0,0))

    #Figuras
    pintarCirculo()
    pintarCuadrado()
    star()

    #Actualizar contenido de la pantalla
    pygame.display.flip()
