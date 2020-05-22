import pygame
from pygame.locals import *
import sys
from colors import *
import random

class Tablero():
  def make(self,w,h):
    self.pcValue = []
    for counter in range(4):
      randomNumber = random.randint(0, 5)
      self.pcValue.append(randomNumber)
    pygame.init()
    title = "Mr. Mind"
    pygame.display.set_caption(title)
    self.widthChecker = 10
    self.dis_w = w
    self.dis_h = h
    self.widthPiece = int(self.dis_w/6) 
    self.display = pygame.display.set_mode((self.dis_w, self.dis_h))
    self.colors = [Aqua,Fuchsia,Red,Yellow,Green,Purple]
    self.colorSelected = self.colors[0]
    self.selectColors = [] # X Start,X END
    self.spaceBtwnH = 0
    self.playGridY = []
    self.playGridX = []
    self.guessedValue = [0,0,0,0]
    self.checkValue = [0,0,0,0]
    self.idxColor = 0
    self.makeGrid(10)
    self.showColors()
    self.colorOK = 1
    self.posOK = 2
    self.won = False
    self.endGame = False

  def finish(self):
    pygame.quit
    sys.exit()

  def makeGrid(self,tries):
    self.makeRows(tries+2) # One for cover one for show colors
    self.makeCols()
    self.currentTry = tries-1

  def makeRows(self,n):
    self.strokeH=5
    self.spaceBtwnH = self.dis_h/n
    self.total_rows = n
    rows = []
    for row in range(n):
      if row != 0:
        self.playGridY.append(self.spaceBtwnH*row)
      pygame.draw.rect(self.display,White,[0,self.spaceBtwnH*(row),self.dis_w,self.strokeH])
    pygame.draw.rect(self.display,Silver,[0,0,self.dis_w,self.spaceBtwnH])
    pygame.display.update()

  def makeCols(self):
    self.strokeV = 2
    self.spaceBtwnV = self.widthPiece - (self.strokeV*2)
    for col in range(5):      
      self.playGridX.append(self.spaceBtwnV*col)
      if col == 4:
        pygame.draw.rect(self.display,Silver,[self.spaceBtwnV*col,self.spaceBtwnH,self.strokeV+4,self.dis_h])
      else:
        pygame.draw.rect(self.display,White,[self.spaceBtwnV*col,self.spaceBtwnH,self.strokeV,self.dis_h])
    self.doneBoundary = self.dis_w-self.spaceBtwnV
    pygame.draw.rect(self.display,White,[self.doneBoundary,self.spaceBtwnH,self.strokeV+2,self.dis_h])

  def showColors(self):
    self.startYColors = self.dis_h - self.spaceBtwnH + self.strokeH
    for box in range(6):
      startBox = self.widthPiece*box
      pygame.draw.rect(self.display,self.colors[box],[startBox,self.startYColors,self.widthPiece,self.widthPiece])
      self.selectColors.append([startBox,startBox+self.widthPiece])
      pygame.display.update() 
  
  def chooseColor(self,x):
    for i in range(6):
      if  x in range(self.selectColors[i][0],self.selectColors[i][1]):
        self.colorSelected = self.colors[i]
        self.idxColor = i

  def printPos(self,pos):
    Y = self.playGridY[self.currentTry]
    X = self.playGridX[pos]
    pygame.draw.rect(self.display,self.colorSelected,[X+self.strokeH/2,Y+self.strokeH,self.spaceBtwnV-self.strokeV/2,self.spaceBtwnH-self.strokeH])
    pygame.display.update() 

  def printDone(self):
    pygame.draw.rect(self.display,Silver,[self.doneBoundary+self.strokeH/2,self.playGridY[self.currentTry]+self.strokeH,self.spaceBtwnV-self.strokeV/2,self.spaceBtwnH-self.strokeH])
    pygame.display.update() 

  def updateGuessed(self,pos,guessed):
    self.guessedValue[pos] = guessed
  
  def printCheckers(self):
    idx = random.sample(range(4), 4)
    startX = self.playGridX[-1] +10
    for i in idx:
      if self.checkValue[i] == self.colorOK:
        colorCheck = White
      elif self.checkValue[i] == self.posOK:
        colorCheck = Lime
      else:
        colorCheck = Black
      pygame.draw.rect(self.display,colorCheck,[startX,self.playGridY[self.currentTry]+10,self.widthChecker,self.widthChecker])
      startX += 13
    pygame.display.update() 

  def uncover(self):
    start = 0
    pcColor = []
    for i in self.pcValue:
      pcColor.append(self.colors[i])
    for box in range(4):
      startBox = self.widthPiece*box
      pygame.draw.rect(self.display,pcColor[box],[startBox,start,self.widthPiece,self.spaceBtwnH])
      self.selectColors.append([startBox,startBox+self.widthPiece])
      pygame.display.update() 

  def disText(self,text,win):
    self.uncover()
    font = pygame.font.Font('freesansbold.ttf', 32)
    if win: 
      text = font.render(text, True, Lime, Blue) 
    else:
      text = font.render(text, True, Purple, Red) 
    textRect = text.get_rect()  
    textRect.center = (self.dis_w// 2, self.dis_h // 2) 
    self.display.blit(text, textRect) 
    pygame.display.update() 

  def splash(self,text,win):
    self.won = win
    self.disText(text,win)

  def checkGuessed(self):
    tmp = self.pcValue.copy()
    for i in range(4): #searching for same color and same position
      if self.guessedValue[i] == self.pcValue[i]:
        self.checkValue[i] = self.posOK
        tmp[i] = 99
        self.guessedValue[i] = 100
    for i in range(4): #searching same color
      found = False
      j = 0
      while(not found):
        if self.guessedValue[i] == tmp[j]:
          self.checkValue[i] = self.colorOK
          tmp[j] = 99
          found = True
        j += 1
        if j== 4:
          found = True
    self.printCheckers()
    if self.checkValue == [2,2,2,2]:
      self.splash("Weeee!!!",True)
    self.checkValue = [0,0,0,0]

  def actionPiece(self,x):
    if x > self.doneBoundary:
      self.printDone()
      self.checkGuessed()
      self.currentTry -= 1
      if (self.currentTry < 0) & (self.won == False):
        self.splash("Buuuu!!",False)
    else:
      for i in range(4):
        if ((x >= self.playGridX[i]) & (x <= self.playGridX[i+1])):
          self.updateGuessed(i,self.idxColor)
          self.printPos(i)
        
  def whereClicked(self,x,y):
    if self.endGame == False:
      if y > self.startYColors:
        self.chooseColor(x)
      elif (y > self.playGridY[self.currentTry]) & (y < self.playGridY[self.currentTry+1]) :
        self.actionPiece(x)