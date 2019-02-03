import pygame

pygame.display.set_caption("ChessMania")



def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255,250,250), (0,0,0)]    # Set up colors [white, black]

    n = len(the_board)
    surface_sz = 580
    sq_sz = surface_sz // n
    surface_sz = n * sq_sz

    surface = pygame.display.set_mode((surface_sz, surface_sz))



    while True:


        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        for row in range(n):
            c_indx = row % 2
            for col in range(n):
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)

                c_indx = (c_indx + 1) % 2

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
