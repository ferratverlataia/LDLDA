import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (171, 171, 171)]
indexColor = 0
def pygame_init():
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Hello world!')
    return windowSurface

def drawCara(windowSurface, cara):
    global colors, indexColor
    arista = cara
    actual = None
    other = arista

    while arista != actual:
        actual = other.siguiente
        origin = other.origin.coord
        coords = actual.origin.coord
        pygame.draw.line(windowSurface, colors[indexColor], (origin.x * 20, origin.y * 20),
                         (coords.x * 20, coords.y * 20), 4)
        other = actual
    indexColor += 1
    if indexColor == len(colors):
        indexColor = 0

def printPoints(windowSurface, ldlda, linea):
    windowSurface.fill(WHITE)
    pygame.draw.line(windowSurface, RED, (0, linea.y*20), (500, linea.y*20), 4)
    print(linea.x, linea.y)

    for i in ldlda:
        caras = i.CARAS
        for key in caras:
            cara = caras[key]
            if cara.cmpint:
                for cmp in cara.cmpint:
                    drawCara(windowSurface, cmp)
            if cara.cmpext:
                for cmp in cara.cmpext:
                    drawCara(windowSurface, cmp)



def pygame_drawtest(windowSurface):
    # set up fonts
    basicFont = pygame.font.SysFont(None, 48)

    # set up the text
    text = basicFont.render('Hello world!', True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    # draw the white background onto the surface
    windowSurface.fill(WHITE)

    # draw a green polygon onto the surface
    pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    # draw some blue lines onto the surface
    pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
    pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

    # draw a blue circle onto the surface
    pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

    # draw a red ellipse onto the surface
    pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

    # draw the text's background rectangle onto the surface
    pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

    # get a pixel array of the surface
    pixArray = pygame.PixelArray(windowSurface)
    pixArray[480][380] = BLACK
    del pixArray

    # draw the text onto the surface
    windowSurface.blit(text, textRect)
    
def pygame_loop(windowSurface):
    pygame.display.update()
    return


