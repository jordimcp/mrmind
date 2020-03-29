import pygame
from pygame.locals import *
from colors import *
import sys 
import random

pygame.init()
title = "Mr. Mind"
pygame.display.set_caption(title)
dis_w = 400
dis_h = 400 
display = pygame.display.set_mode((dis_w, dis_h))

#Cover
coverSpace=60
pygame.draw.rect(display,Gray,[0,0,dis_w,coverSpace])
codedValue = []
for counter in range(4):
  randomNumber = random.randint(0, 5)
  codedValue.append(randomNumber)

#Grid
h=5
spaceBtwnH = 30
colorBoxsStart = dis_h - spaceBtwnH
colorBoxWidth = int(dis_w/6)
rows = []
for row in range(11):
  pygame.draw.rect(display,White,[0,spaceBtwnH*(row)+coverSpace,dis_w,h])
  rows.append(row+(spaceBtwnH*(row)+coverSpace))

pygame.draw.rect(display,Silver,[dis_w-30,0,5,dis_h])
done = dis_w-30
for col in range(5):
  pygame.draw.rect(display,Gray,[col*colorBoxWidth,0,5,colorBoxsStart])
playerGrid = []
for row in range(10):
  for col in range(4):
    start = (col*colorBoxWidth)
    end = start + (colorBoxWidth)
    playerGrid.append([start,end,col,row,99])

#Colors in play
colors = [Aqua,Fuchsia,Red,Yellow,Green,Purple]
colorsArea = []
for box in range(6):
  pygame.draw.rect(display,colors[box],[colorBoxWidth*box,colorBoxsStart,colorBoxWidth,colorBoxWidth])
  boxIni = colorBoxWidth*box
  boxEnd = colorBoxWidth + boxIni
  colorsArea.append([boxIni,boxEnd])

pygame.display.update()
colorSelected = Black
ColorOK = 1
PosOK = 2
currentRow = 9
decodeValue = [199,199,199,199]
checkValue = [0,0,0,0]

def disText(text,win):
  font = pygame.font.Font('freesansbold.ttf', 32)
  if win: 
    text = font.render(text, True, Lime, Blue) 
  else:
    text = font.render(text, True, Purple, Red) 
  textRect = text.get_rect()  
  textRect.center = (dis_w// 2, dis_h // 2) 
  display.blit(text, textRect) 

while True: # main game lo
    if currentRow < 0:
      disText("Buuuu!!",False)
      for i in range(4):
        colorEnd = colors[codedValue[i]]
        pygame.draw.rect(display,colorEnd,[colorBoxWidth*i,0,colorBoxWidth,colorBoxWidth])
      pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          x = pos[0]
          y = pos[1]
          if (y > rows[currentRow]) & (y < rows[currentRow+1]) :
            for i in range(40):
              if playerGrid[i][3] == currentRow:
                if x in range(playerGrid[i][0],playerGrid[i][1]-1):
                  if colorSelected != Black:
                    xst=playerGrid[i][0]
                    pygame.draw.rect(display,colorSelected,[xst,rows[currentRow],colorBoxWidth,spaceBtwnH])
                    playerGrid[i][4] = colorSelected
                    decodeValue[playerGrid[i][2]] = colSelected
                    pygame.display.update()
                if x > done:
                  tmp = codedValue.copy()
                  for i in range(4):
                    if decodeValue[i] == codedValue[i]:
                      checkValue[i] = PosOK
                      tmp[i] = 99
                      decodeValue[i] = 100
                  for i in range(4):
                    found = False
                    j = 0
                    while(not found):
                      if decodeValue[i] == tmp[j]:
                        checkValue[i] = ColorOK
                        tmp[j] = 99
                        found = True
                      j += 1
                      if j== 4:
                        found = True
                  idx = random.sample(range(4), 4)
                  init = done-100
                  for i in idx:
                    if checkValue[i] == ColorOK:
                      colorCheck = White
                    elif checkValue[i] == PosOK:
                      colorCheck = Lime
                    else:
                      colorCheck = Black
                    pygame.draw.rect(display,colorCheck,[init,rows[currentRow],10,10])
                    pygame.display.update()
                    init +=15
                  pygame.draw.rect(display,Silver,[done,rows[currentRow],colorBoxWidth,spaceBtwnH])
                  if checkValue == [2,2,2,2]:
                    for i in range(4):
                      colorEnd = colors[codedValue[i]]
                      pygame.draw.rect(display,colorEnd,[colorBoxWidth*i,0,colorBoxWidth,colorBoxWidth])
                    disText("Weee!!!",True)
                  pygame.display.update()
                  currentRow -= 1
                  decodeValue = [199,199,199,199]
                  checkValue = [0,0,0,0]

          if y > colorBoxsStart:
            for i in range(6):
              if  x in range(colorsArea[i][0],colorsArea[i][1]):
                colorSelected = colors[i]
                colSelected = i
