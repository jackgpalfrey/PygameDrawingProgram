import pygame
from Utils.RGBcolors import AllColors as Color
import random

WIDTH = 800
HEIGHT = 800

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Drawing Program")
win.fill(Color.WHITE)

# Hello
pygame.init()
pygame.font.init()


running = True



class DrawSurface():
    def __init__(self,win,surfaceWidth,surfaceHeight,surfaceXOffset,surfaceYOffset,pixelXDensity,pixelYDensity):
        self.win = win
        self.width = surfaceWidth
        self.height = surfaceHeight
        self.xOffset = surfaceXOffset
        self.yOffset = surfaceYOffset
        self.xDensity = pixelXDensity
        self.yDensity = pixelYDensity
        self.baseColor = Color.PINK


        self.createPixelGrid(self.width,self.height,self.xDensity,self.yDensity)

    def createPixelGrid(self,surfaceWidth,surfaceHeight,xPixelDensity,yPixelDensity):
        pixelGrid = []

        self.xPixelSize = surfaceWidth / xPixelDensity
        self.yPixelSize = surfaceHeight / yPixelDensity



        for row in range(xPixelDensity):
            pixelGrid.append([])
            for pixel in range(yPixelDensity):
                pixelGrid[row].append(self.baseColor)


        self.pixelGrid = pixelGrid


    def getPixelGird(self):
        print(self.pixelGrid)



    def draw(self):
        for row in range(len(self.pixelGrid)):
            xPos = self.xOffset + (row * self.xPixelSize)
            for pixel in range(len(self.pixelGrid[row])):
                yPos = self.yOffset + (pixel * self.yPixelSize) 
                color = self.pixelGrid[row][pixel]
                pygame.draw.rect(self.win, color, (xPos,yPos,self.xPixelSize,self.yPixelSize))

        pygame.draw.line(self.win,Color.GREY,(self.xOffset, self.yOffset),(self.xOffset, self.yOffset + self.height))
        pygame.draw.line(self.win,Color.GREY,(self.xOffset + self.width ,self.yOffset),(self.xOffset + self.width, self.yOffset + self.height))
        pygame.draw.line(self.win,Color.GREY,(self.xOffset,self.yOffset + self.height),(self.xOffset + self.width, self.yOffset + self.height))
        pygame.draw.line(self.win,Color.GREY,(self.xOffset,self.yOffset),(self.xOffset + self.width, self.yOffset))


    def getMousedPixel(self,mousePos):
        x,y = mousePos

        row = int((x - self.xOffset) // self.xPixelSize)
        col = int((y - self.yOffset) // self.yPixelSize)

        print(row, " - ", self.xDensity)
        print(col, " - ", self.yDensity)

        if row < self.xDensity and row >= 0 and col < self.yDensity and col >= 0:
            return [row,col]
        else:
            checkMenuPos(mousePos)
            raise Exception("Outside of pixel Grid")


    def changeColor(self,pos,color):
        try:
            coords = self.getMousedPixel(pos)
        except Exception:
            print("Nah")
            return False
        else:
            if color == "ERASER":
                color = self.baseColor
            self.pixelGrid[coords[0]][coords[1]] = color

def drawMenu():

    font = pygame.font.Font('freesansbold.ttf', 20) 
    
    pygame.draw.rect(win, Color.GREY, (50,675,100,50)) # Clear
    pygame.draw.rect(win, Color.GREY, (650,675,100,50)) # Rubber
    pygame.draw.rect(win, Color.RED, (325,675,50,50))
    pygame.draw.rect(win, Color.ORANGE, (325,725,50,50))
    pygame.draw.rect(win, Color.BLUE, (375,675,50,50)) #
    pygame.draw.rect(win, Color.GREEN, (375,725,50,50))
    pygame.draw.rect(win, Color.BLACK, (425,675,50,50))
    pygame.draw.rect(win, Color.WHITE, (425,725,50,50))
    text = font.render('Clear', True, Color.BLACK) 
    textRect = text.get_rect()
    win.blit(text, (50 + ((100  - textRect.width)// 2),675 + ((50 - textRect.height)//2)))
    text = font.render('Eraser', True, Color.BLACK) 
    textRect = text.get_rect()
    win.blit(text, (650 + ((100  - textRect.width)// 2),675 + ((50 - textRect.height)//2)))

    pygame.draw.line(win,Color.BLACK,(325, 675),(475, 675))
    pygame.draw.line(win,Color.BLACK,(325, 775),(475, 775))
    pygame.draw.line(win,Color.BLACK,(325, 675),(325, 775))
    pygame.draw.line(win,Color.BLACK,(475, 675),(475, 775))


paintColor = Color.BLACK

def checkMenuPos(pos):
    global paintColor
    x,y = pos

    if x >= 50 and x <= 150 and y >= 675 and y <= 725 :
        surf.createPixelGrid(700,600,70,60)
    elif x >= 325 and x <= 375 and y >= 675 and y <= 725 :
        paintColor = Color.RED
    elif x >= 375 and x <= 425 and y >= 675 and y <= 725 :
        paintColor = Color.BLUE
    elif x >= 300 and x <= 350 and y >= 725 and y <= 775 :
        paintColor = Color.ORANGE
    elif x >= 375 and x <= 425 and y >= 725 and y <= 775 :
        paintColor = Color.GREEN
    elif x >= 425 and x <= 475 and y >= 675 and y <= 725 :
        paintColor = Color.BLACK
    elif x >= 425 and x <= 475 and y >= 725 and y <= 775 :
        paintColor = Color.WHITE
    elif x >= 650 and x <= 750 and y >= 675 and y <= 725 :
        paintColor = "ERASER"
    
    
surf = DrawSurface(win,700,600,50,50,70,60)


surf.draw()

pygame.display.update()




while running:

    surf.draw()
    drawMenu()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            surf.changeColor(pos,paintColor)
        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            surf.changeColor(pos,"ERASER")


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                surf.createPixelGrid(700,600,70,60)
                pass
            elif event.key == pygame.K_BACKSPACE:
                paintColor = "ERASER"
            elif event.key == pygame.K_1:
                paintColor = Color.BLUE
            elif event.key == pygame.K_2:
                paintColor = Color.RED
