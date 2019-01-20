import pygame
from board.chessBoard import Board

pygame.init()
gamedisplay = pygame.display.set_mode((700,700))
pygame.display.set_caption("ChessMania")
clock = pygame.time.Clock()


chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

allTiles = []
allPieces = []

def squares(x,y,w,h,colour):
    pygame.draw.rect(gameDisplay,colour,[x,y,w,h])
    allTiles.append([colour,[x,y,w,h]])




def drawChessPieces()
    xpos = 0
    ypos = 0
    colour = 0
    width = 100
    height = 100
    black = (66,134,244)
    white = (143,155,175)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if colour % 2 == 0:
                squares(xpos, ypos, width height, white)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-'
                    img = pygame.image.load("./chessArt/" + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + chessBoard.gameTiles[number].pieceOnTile.toString().upper()+ ".jpg")

                    img = pygame.transform.scale(img, (100,100))
                    allPieces.append([img, [xpos,ypos], chessBoard.gameTiles[number].pieceOnTile])

                xpos += 100

            else:
                squares(xpos, ypos, width height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-'
                    img = pygame.image.load("./chessArt/" + chessBoard.gameTiles[number].pieceOnTile.alliance[0].upper() + chessBoard.gameTiles[number].pieceOnTile.toString().upper()+ ".jpg")

                    img = pygame.transform.scale(img, (100,100))
                    allPieces.append([img, [xpos,ypos], chessBoard.gameTiles[number].pieceOnTile])

                xpos += 100

            colour += 1
            number += 1

        colour += 1
        xpos = 0
        ypos += 100



quitgame = False

while not quitgame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    for img in allPieces:
        gamedisplay.blit(img[0], img[1])

    pygame.display.update()
    clock.tick(60)
