import pygame, sys, random
import tictactoeInit as init
import numpy as np

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

def handle_inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            init.clicked_x = int(event.pos[1]//init.row_size)
            init.clicked_y = int(event.pos[0]//init.row_size)
            mark_square()
def draw_lines():

    pygame.draw.line(screen, init.line_colour, init.h1_start, init.h1_end, init.line_width)
    pygame.draw.line(screen, init.line_colour, init.h2_start, init.h2_end, init.line_width)

    pygame.draw.line(screen, init.line_colour, init.v1_start, init.v1_end, init.line_width)
    pygame.draw.line(screen, init.line_colour, init.v2_start, init.v2_end, init.line_width)
def draw_board():
    for i in range(0, 3):
        for j in range(0, 3):
            if init.board[i][j] == 1: # draw circle
                pygame.draw.circle(screen, init.circle_clr, (int(j * init.row_size + init.row_size/2), int(i * init.col_size + init.col_size/2)), init.circle_radius, init.circle_width)
            elif init.board[i][j] == 2: # draw cross
                pygame.draw.line(screen, init.cross_clr, (init.line1_start(i, j)), (init.line1_end(i, j)), init.cross_width)
                pygame.draw.line(screen, init.cross_clr, (init.line2_start(i, j)), (init.line2_end(i, j)), init.cross_width)
def mark_square():
    if init.board[init.clicked_x][init.clicked_y] == 0:
        init.board[init.clicked_x][init.clicked_y] = init.player
        if not init.game_over:
            pygame.mixer.Sound.play(init.draw_sound)

        if init.player == 1:
            init.player = 2
            init.winner = 1
            init.win_line_colour = init.circle_clr
        else:
            init.player = 1
            init.winner = 2
            init.win_line_colour = init.cross_clr
def check_win():

    # check horizontally
    for num in range(0, 3):
        if init.hor_win(num):
            pygame.mixer.Sound.play(init.draw_sound)
            pygame.draw.line(screen, init.win_line_colour, (init.hor_start()), (init.hor_end()), 15)
            init.game_over = True

        elif init.ver_win(num):
            pygame.mixer.Sound.play(init.draw_sound)
            pygame.draw.line(screen, init.win_line_colour, (init.ver_start()), (init.ver_end()), 15)
            init.game_over = True

        elif init.diag_win():
            pygame.mixer.Sound.play(init.draw_sound)
            pygame.draw.line(screen, init.win_line_colour, (init.diag_start()), (init.diag_end()), 25)
            init.game_over = True
def check_draw():
    if init.game_over:
        return
    for i in range(0, 3):
        for j in range(0, 3):
            if init.board[i][j] == 0:
                return
    flash_lines()
    pygame.mixer.Sound.play(init.tie_sound)
    pygame.time.delay(500)
    draw_lines()

    flash_lines()
    pygame.mixer.Sound.play(init.tie_sound)
    pygame.time.delay(500)
    draw_lines()

    # Display Game Over screen
    screen.fill(init.bg_color)
    text1 = init.text_font.render("GAME OVER", False, init.light_grey)
    screen.blit(text1, (init.GO1_x, init.GO1_y))
    pygame.display.flip()

    init.game_over = True
def flash_lines():
    screen.fill(init.bg_color)
    draw_board()
    pygame.display.flip()

    pygame.time.wait(500)
    #
    draw_lines()
    pygame.display.flip()

# Screen
screen = pygame.display.set_mode((init.screen_width, init.screen_height))
pygame.display.set_caption("TicTacToe")

# Main Game Loop
while True:
    if init.game_over:
        handle_inputs()
    else:
        handle_inputs()
        screen.fill(init.bg_color)
        draw_lines()
        draw_board()
        check_win()
        check_draw()

    pygame.display.flip()
    clock.tick(60)
