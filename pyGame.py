# this draws the mat and line of the were the robot went

import pygame
import math


def runGame(positions):
    '''
    this takes positons from the robots's memory to draw lines on a
    picture of the mat on the screen 
    '''


    # these are the width and hieht of the mat and table in cms
    tableWidth = 236
    tableHeight = 114
    matWidth = 202
    matStartCms = 34
    tableRatio = tableWidth / tableHeight
    matRatio = matWidth / tableHeight

    # this tells it how big to make the piture in pixels
    displayWidth = 1500
    displayHeight = int(displayWidth * (1 / tableRatio))

    lineWidth = 10 #pixels

    # this converts cms to pixels
    tableScreenRatio = tableWidth / displayWidth
    matStartPixels = int(matStartCms * (1 / tableScreenRatio))
    matDisplayHeight = int(displayHeight)
    matDisplayWidth = int(matDisplayHeight * matRatio)


    # turn bot coords to screen corrds
    # cms -> pixels
    # switch y direction
    displayPositions = []
    for i in range(len(positions)):
        pos = positions[i]
        # newPos = (pos[0] / tableScreenRatio, (pos[1] / tableScreenRatio))
        newPosX = (pos[0] / tableScreenRatio)
        newPosY = displayHeight - (pos[1] / tableScreenRatio)
        newPos = (newPosX, newPosY)

        print("newPos", newPos)
        displayPositions.append(newPos)


     # colors
    black = (0,0,0)
    white = (255,255,255)
    darkRed = (200, 0, 0)

    # this makes the window to show the picture, and it makes it the size we set earlyer 
    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('EV3 python simulation')

     # setup display with matt
    fn = "/Users/pmargani/Downloads/fllReplayMat2.jpg"
    matImg = pygame.image.load(fn)
    matImg = pygame.transform.scale(matImg, (matDisplayWidth, matDisplayHeight))

    # Grab img for animation 
    fn = "data/robotPic1.jpg"
    botImg = pygame.image.load(fn)
    botImg = pygame.transform.scale(botImg, (100, 100))

    # set it up to move on it's first line
    deg2rad = (math.pi/180.0)
    botX = displayPositions[0][0]
    botY = displayPositions[0][1]
    botX2 = displayPositions[1][0]
    botY2 = displayPositions[1][1]
    botAngle = math.tanh((botY2 - botY)/(botX2 - botX)) / deg2rad
    botSpeed = 0.5
    
    running = True
    while running:

        # quit?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Display mat
        # this is were we make the background a color and draws a Picture 
        gameDisplay.fill(white)
        gameDisplay.blit(matImg, (matStartPixels, 0))

        # display bot
        # gameDisplay.blit(botImg, (int(botX), int(botY)))

        # update bot position
        speedX = botSpeed * math.cos(deg2rad*botAngle)
        speedY = botSpeed * math.sin(deg2rad*botAngle)
        # if int(botX) == int(botX2) and int(botY) == int(botY2):
        if abs(botX - botX2) < 3 and abs(botY - botY2) < 3:
            # we got to the end of the line!
            speedX = 0
            speedY = 0
        botX = botX + (speedX * 1)
        botY = botY + (speedY * 1)

        # display positions:
        for i in range(len(displayPositions)-1):
            pygame.draw.line(gameDisplay, darkRed, displayPositions[i], displayPositions[i+1], width=lineWidth)
            
        pygame.display.update()



if __name__ == '__main__':
    positions = [
        (34, 10),
        (34 + 101, 10)
        # (0, 0),
        # (100, 100),
        # (500, 100)
    ]
    runGame(positions)