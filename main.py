import pygame
from pygame.locals import *


def check_cell(cell, cells, remove, neighbourhood):
    neighbours = 0
    for row in range(cell[1]-1, cell[1]+2):
        for column in range(cell[0]-1, cell[0]+2):
            if (column, row) != cell and (column, row) in cells:
                neighbours += 1
            elif (column, row) != cell and (column, row) not in neighbourhood:
                neighbourhood.append((column, row))
    if neighbours < 2:
        remove.append(cell)
    elif neighbours == 2 or neighbours == 3:
        pass
    elif neighbours > 3:
        remove.append(cell)


def check_dead(cell, cells, add):
    neighbours = 0
    for row in range(cell[1] - 1, cell[1] + 2):
        for column in range(cell[0] - 1, cell[0] + 2):
            if (column, row) != cell and (column, row) in cells:
                neighbours += 1

    if neighbours == 3:
        add.append(cell)


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Conway's Game Of Life")

    game_clock = pygame.time.Clock()

    cells = [(2,5), (2,6), (3,5), (3,6), (10,5), (10,6), (10,7), (11,4), (11,8), (12,3), (13,3), (12,9), (13,9),
             (14,6), (15,4), (15,8), (16,5), (16,6), (16,7), (17,6)]
    add = []
    remove = []
    ini_cells = []
    width = 20
    height = 20
    xcoord = 10
    ycoord = 10
    speed = 10
    fps = 0
    frame = 0
    speed = 3
    move_l = False
    move_r = False
    move_u = False
    move_d = False
    play = False
    zoom_up = False
    zoom_down = False
    speed_up = False
    speed_down = False
    reset = False

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    #text = font.render("Hello There", 1, (10, 10, 10))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for cell in cells:
        ini_cells.append(cell)

    # Event loop
    while 1:
        current_time = pygame.time.get_ticks()
        neighbours = []
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(str(event.key))
            if event.type == pygame.KEYDOWN and event.key == K_a:
                move_l = True
            if event.type == pygame.KEYUP and event.key == K_a:
                move_l = False
            if event.type == pygame.KEYDOWN and event.key == K_d:
                move_r = True
            if event.type == pygame.KEYUP and event.key == K_d:
                move_r = False
            if event.type == pygame.KEYDOWN and event.key == K_w:
                move_u = True
            if event.type == pygame.KEYUP and event.key == K_w:
                move_u = False
            if event.type == pygame.KEYDOWN and event.key == K_s:
                move_d = True
            if event.type == pygame.KEYUP and event.key == K_s:
                move_d = False
            if event.type == pygame.KEYDOWN and event.key == K_UP:
                zoom_up = True
            if event.type == pygame.KEYUP and event.key == K_UP:
                zoom_up = False
            if event.type == pygame.KEYDOWN and event.key == K_DOWN:
                zoom_down = True
            if event.type == pygame.KEYUP and event.key == K_DOWN:
                zoom_down = False
            if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                speed_up = True
            if event.type == pygame.KEYUP and event.key == K_RIGHT:
                speed_up = False
            if event.type == pygame.KEYDOWN and event.key == K_LEFT:
                speed_down = True
            if event.type == pygame.KEYUP and event.key == K_LEFT:
                speed_down = False
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                play = not play
            if event.type == pygame.KEYDOWN and event.key == K_r:
                add = []
                remove = []
                neighbours = []
                cells = []
                play = False
                for cell in ini_cells:
                    cells.append(cell)

            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                pygame.quit()
                return
        if move_l:
            xcoord -= 1 * speed
        if move_r:
            xcoord += 1 * speed
        if move_u:
            ycoord += 1 * speed
        if move_d:
            ycoord -= 1 * speed
        if zoom_up:
            width += 1
            height += 1
        if zoom_down:
            width -= 1
            height -= 1
        if speed_up:
            if speed > 1:
                speed -= 1
        if speed_down:
            if speed < 15:
                speed += 1

        if play and not reset and frame % speed == 0:
            print(int(fps))
            if len(cells) > 0:
                for cell in cells:
                    check_cell(cell, cells, remove, neighbours)

            if len(neighbours) > 0:
                for neighbour in neighbours:
                    check_dead(neighbour, cells, add)

            if len(remove) > 0:
                for dead in remove:
                    if dead in cells:
                        cells.remove(cells[cells.index(dead)])
                remove = []

            if len(add) > 0:
                for alive in add:
                    if alive not in cells:
                        cells.append(alive)
                add = []

        if len(cells) > 0:
            background.fill((255,255,255))
            for cell in cells:
                pygame.draw.rect(background, (0,0,0),
                                 pygame.Rect(cell[0]*width - xcoord, cell[1]*height + ycoord, width, height))
        else:
            background.fill((255, 255, 255))


        #screen.fill((255,255,255))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        game_clock.tick(60)
        past_time = current_time
        current_time = pygame.time.get_ticks()
        spf = current_time - past_time
        fps = 1000 / spf
        frame += 1
        print(frame)
        if frame == int(fps):
            frame = 0




if __name__ == '__main__': main()
