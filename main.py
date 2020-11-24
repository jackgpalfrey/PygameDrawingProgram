# Imports
import pygame
from Utils.RGBcolors import AllColors as Color
import random

# Constants:
WIDTH = 800
HEIGHT = 800

# Pygame Initialisations
pygame.init()
pygame.font.init()

# Create Window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Drawing Program")
win.fill(Color.WHITE)

# Class for DrawingSurface
class DrawSurface():
    def __init__(self,win,surfaceWidth,surfaceHeight,surfaceXOffset,surfaceYOffset,pixelXDensity,pixelYDensity):
        """ Creates Drawing Surface

        Args:
            win (Surface): Base Game Window
            surfaceWidth (int): Width of drawing surface
            surfaceHeight (int): Height of drawing surface
            surfaceXOffset (int): Offset of the drawing surface from the left of the screen
            surfaceYOffset (int): Offset of the drawing surface from the top of the screen
            pixelXDensity (int): Number of pixels on the x axis
            pixelYDensity (int): Number of pixels on the y axis
        """
        self.win = win
        self.width = surfaceWidth
        self.height = surfaceHeight
        self.xOffset = surfaceXOffset
        self.yOffset = surfaceYOffset
        self.xDensity = pixelXDensity
        self.yDensity = pixelYDensity
        self.baseColor = Color.LIGHT_GREY # Color all pixels will start as


        self.pixelGrid = self.createPixelGrid(self.width,self.height,self.xDensity,self.yDensity)

    def createPixelGrid(self,surfaceWidth,surfaceHeight,xPixelDensity,yPixelDensity):
        """ Creates the array data structure for the Drawing Surface

        Args:
            surfaceWidth (int): Width of the drawing surface
            surfaceHeight (int): Height of the drawing
            xPixelDensity (int): Number of pixels on the x axis
            yPixelDensity (int): Number of pixels on y axis

        Returns:
            array: array data structure of drawing surface
        """
        pixelGrid = [] # Creates array


        # Gets pixel size
        self.xPixelSize = surfaceWidth / xPixelDensity
        self.yPixelSize = surfaceHeight / yPixelDensity


        # Loops through each pixel and creates a related position in the array
        for row in range(xPixelDensity):
            pixelGrid.append([])
            for pixel in range(yPixelDensity):
                pixelGrid[row].append(self.baseColor)

        return pixelGrid


    def getPixelGird(self):
        """ Returns the pixelGrid of the DrawSurface Class
        """
        print(self.pixelGrid)



    def draw(self):
        """ Draws each pixel in the pixelGrid and the border around the Drawing Surface
        """
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
        """ Works out based on pygame mouse coordinates the pixel in the Drawing Surface the point is in

        Args:
            mousePos (tuple): Position of mouse (x,y)

        Raises:
            Exception: Raises if mouse position is outside of the pixel grid

        Returns:
            tuple : the [row,col] of the pixel its in
        """
        x,y = mousePos # Converts tuple to x and y variable

        # Works out row and col
        row = int((x - self.xOffset) // self.xPixelSize)
        col = int((y - self.yOffset) // self.yPixelSize)

        # Checks if row and col is inside Draw Surface
        if row < self.xDensity and row >= 0 and col < self.yDensity and col >= 0:
            return [row,col]
        else: # Else raises Exception
            raise Exception("Outside of pixel Grid")


    def changeColor(self,gridPos,color):
        """ Changes Color of a given gridPixel

        Args:
            gridPos (tuple): Position in grid of pixel
            color (tuple): Wanted RGB color of pixel
        """
        if color == "ERASER": # Checks if color is ERASER if so sets color to the base color of the Draw Surface
            color = self.baseColor
        self.pixelGrid[gridPos[0]][gridPos[1]] = color


def drawMenu():
    """ Draws Menu Elements of the Application
    """
    font = pygame.font.Font('freesansbold.ttf', 20) # Loads font used in menu
    
    # Clear Button
    pygame.draw.rect(win, Color.GREY, (50,675,100,50)) # Creates Button Box
    text = font.render('Clear', True, Color.BLACK) # Creates Text
    textRect = text.get_rect() # Gets Bounds of Text
    win.blit(text, (50 + ((100  - textRect.width)// 2),675 + ((50 - textRect.height)//2))) # Draws Text

    # Eraser Button
    pygame.draw.rect(win, Color.GREY, (650,675,100,50)) # Creats Button Box
    text = font.render('Eraser', True, Color.BLACK) # Creates Text
    textRect = text.get_rect() # Gets Bounding Box
    win.blit(text, (650 + ((100  - textRect.width)// 2),675 + ((50 - textRect.height)//2))) # Draws Text

    # Color Selectors
    pygame.draw.rect(win, Color.RED, (325,675,50,50)) # Red Color Button
    pygame.draw.rect(win, Color.ORANGE, (325,725,50,50)) # Orange Color Button
    pygame.draw.rect(win, Color.BLUE, (375,675,50,50)) # Blue Color Button
    pygame.draw.rect(win, Color.GREEN, (375,725,50,50)) # Green Color Button
    pygame.draw.rect(win, Color.BLACK, (425,675,50,50)) # Black Color Button
    pygame.draw.rect(win, Color.WHITE, (425,725,50,50)) # White Color Button
    
    # Draws Border Around Color Selector
    pygame.draw.line(win,Color.BLACK,(325, 675),(475, 675))
    pygame.draw.line(win,Color.BLACK,(325, 775),(475, 775))
    pygame.draw.line(win,Color.BLACK,(325, 675),(325, 775))
    pygame.draw.line(win,Color.BLACK,(475, 675),(475, 775))


def checkMenuPos(mousePos):
    """ Takes Pixel Position of Mouse and finds what menu item has been clicked on

    Args:
        pos (tuple): Pixel Position of mouse
    """
    global paintColor
    x,y = mousePos

    if x >= 50 and x <= 150 and y >= 675 and y <= 725 : # Clear Button
        surf.createPixelGrid(700,600,70,60)
    elif x >= 650 and x <= 750 and y >= 675 and y <= 725 : # Eraser Button
        paintColor = "ERASER"
    elif x >= 325 and x <= 375 and y >= 675 and y <= 725 : # Red Button
        paintColor = Color.RED
    elif x >= 300 and x <= 350 and y >= 725 and y <= 775 : # Orange Button
        paintColor = Color.ORANGE
    elif x >= 375 and x <= 425 and y >= 675 and y <= 725 : # Blue Button
        paintColor = Color.BLUE
    elif x >= 375 and x <= 425 and y >= 725 and y <= 775 : # Green Button
        paintColor = Color.GREEN
    elif x >= 425 and x <= 475 and y >= 675 and y <= 725 : # Black Button
        paintColor = Color.BLACK
    elif x >= 425 and x <= 475 and y >= 725 and y <= 775 : # White Button
        paintColor = Color.WHITE
    
    
def clickHandler(drawSurface,mousePos,paintColor):
    """ Handles Mouse postion and clicks

    Args:
        drawSurface (Surface): Game Window
        mousePos (tuple): Pixel Position of mouse
        paintColor (tuple): RGB color value
    """
    try: # Tries to get the pixelGrid coords of mouse
        gridPos = drawSurface.getMousedPixel(mousePos)
    except Exception: # If coords is outside of pixelGrid runs checkMenuPos() to determine if it clicked a menu item
        checkMenuPos(mousePos)
    else: # If mousePos is inside pixelGrid runs DrawSurface.changeColor() to change the color of selected DrawSurface pixel to paintColor
        surf.changeColor(gridPos,paintColor)


# Creates DrawSurface
surf = DrawSurface(win,700,600,50,50,70,60)
surf.draw()
pygame.display.update()

paintColor = Color.BLACK # Sets Default paintColor to black

# Main Game Loop
running = True
while running:

    # Draws UI
    surf.draw()
    drawMenu()
    pygame.display.update()

    # Event Handling: 
    for event in pygame.event.get():
        # QUIT handling
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()

        # Mouse Handling
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            clickHandler(surf,pos,paintColor)
        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            clickHandler(surf,pos,"ERASER")

        # Key Handling
        elif event.type == pygame.KEYDOWN:
            # Space to Clear Handling
            if event.key == pygame.K_SPACE:
                surf.createPixelGrid(700,600,70,60)

            # Backspace to Select Eraser Handling
            elif event.key == pygame.K_BACKSPACE:
                paintColor = "ERASER"
