import pygame

def runGame(positions):


    print("len:", len(positions))
    print("range: ", range(3))
    for i in range(len(positions)-1):
        print(i)
        print(positions[i])
        print("draw from position i to position i + 1")
        print(positions[i], positions[i+1])

    tableWidth = 236
    tableHeight = 114
    matWidth = 202
    matStartCms = 34
    tableRatio = tableWidth / tableHeight
    matRatio = matWidth / tableHeight

    displayWidth = 1500
    displayHeight = int(displayWidth * (1 / tableRatio))

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

    gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('EV3 python simulation')

     # setup display with matt
    fn = "/Users/pmargani/Downloads/fllReplayMat2.jpg"
    matImg = pygame.image.load(fn)
    matImg = pygame.transform.scale(matImg, (matDisplayWidth, matDisplayHeight))


    running = True
    while running:

        # quit?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Display mat
        gameDisplay.fill(white)
        gameDisplay.blit(matImg, (matStartPixels, 0))

        # display positions:
        for i in range(len(displayPositions)-1):
            pygame.draw.line(gameDisplay, black, displayPositions[i], displayPositions[i+1])
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