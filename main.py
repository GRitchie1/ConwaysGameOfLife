import pygame
import time
import random
import numpy as np
import os
import grid
from image import Image_Array
import math

os.environ["SDL_VIDEO_CENTERED"]='1'

image = Image_Array("input.png")
#image = Image_Array("cat.png")
array = image.getArray()

#resolution
pixels = image.imageSizes()
height, width = pixels[0],pixels[1]

ratio = width/height

if width > height:
    scaler=math.floor(1980/width)
else:
    scaler=math.floor(1080/width)

#scaler = 2


print(ratio)

size = (width*scaler, height*scaler)

print(size)

pygame.init()
pygame.font.init()
textFont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

offset = 1

Grid = grid.Grid(width,height, scaler, offset, colour = True)
Grid.setArray(array)

manualpause = False
pause = False
run = True
started = 0
iteration = 0
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                manualpause = not pause
    

    if started <= 60:
        started += 1
        pause = True
    else:
        if pause != True:
            iteration += 1
            
        if manualpause:
            pause = True
        else:
            pause = False   

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    pygame.draw.rect(screen, black, pygame.Rect(0, 0, width*scaler, 40))
    textsurface = textFont.render(str(iteration), False, (255, 0, 0))
    screen.blit(textsurface,(0,0)) 

    #if pygame.mouse.get_pressed()[0]:
    #    mouseX, mouseY = pygame.mouse.get_pos()
    #    Grid.HandleMouse(mouseX, mouseY)


    pygame.display.update()
    
pygame.quit()