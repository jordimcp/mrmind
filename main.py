from tablero import Tablero
import pygame
from pygame.locals import *

if __name__ == "__main__":
  tablero = Tablero()
  tablero.make(400,400)
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        tablero.finish()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        tablero.whereClicked(x,y)