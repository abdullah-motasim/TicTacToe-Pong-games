# SCREEN
import pygame
import numpy as np

pygame.init()
pygame.font.init()

screen_width = 700
screen_height = 700
bg_color = (28, 170, 156)


# BOARD
rows = 3
cols = 3
board = np.zeros((rows, cols))

player = 2 # 1=O, 2=X
clicked_x = 0
clicked_y = 0
col_size = screen_width // 3
row_size = screen_height // 3


# LINES
line_colour = (23, 145, 135)
line_width = 15
win_line_colour = (255, 255, 255)

# horizontal
offset = 30
h1_start = (offset, row_size)
h1_end = (screen_width-offset, row_size)
h2_start = (offset, row_size*2)
h2_end = (screen_width-offset, row_size*2)

# vertical
v1_start = (col_size, offset)
v1_end = (col_size, screen_height-offset)
v2_start = (col_size*2, offset)
v2_end = (col_size*2, screen_height-offset)


# CIRCLE
circle_clr = pygame.Color(239, 231, 200)
circle_radius = 60
circle_width = 15


# CROSS
cross_clr = (66, 66, 66)
cross_width = 25
cross_space = 55

def line1_start(row, col):
    return (col * row_size + cross_space, row * col_size + col_size - cross_space)

def line1_end(row, col):
    return (col * row_size + row_size - cross_space, row * col_size + cross_space)

def line2_start(row, col):
    return col * row_size + cross_space, row * col_size + cross_space

def line2_end(row, col):
    return col * row_size + row_size - cross_space, row * row_size + row_size - cross_space

# AUDIO
draw_sound = pygame.mixer.Sound("C:/Users/abdul/PycharmProjects/game/tictactoe/audio/draw.mp3")
tie_sound = pygame.mixer.Sound("C:/Users/abdul/PycharmProjects/game/tictactoe/audio/tie.wav")

# WINNING
winner = 1
game_over = False

def hor_win(num):
    if board[num][0] == winner and board[num][1] == winner and board[num][2] == winner:
        return True
    return False
def hor_start():
    return 30, clicked_x * row_size + row_size // 2

def hor_end():
    return screen_width - 30, clicked_x * row_size + row_size // 2


def ver_win(num):
    if board[0][num] == winner and board[1][num] == winner and board[2][num] == winner:
        return True
    return False
def ver_start():
    return clicked_y * row_size + row_size // 2, 30

def ver_end():
    return clicked_y * row_size + row_size // 2, screen_width - 30

def diag_win():
    if board[0][0] == winner and board[1][1] == winner and board[2][2] == winner:
        return True
    elif board[0][2] == winner and board[1][1] == winner and board[2][0] == winner:
        return True
    return False

def diag_start():
    if board[0][0] == winner: #drawing descending diagonal
        return 40, 40
    return 40, screen_height - 40

def diag_end():
    if board[0][0] == winner:  # drawing descending diagonal
        return screen_width - 40, screen_height - 40
    return screen_width - 40, 40

#TEXT
text_font = pygame.font.Font("freesansbold.ttf", 64)
GO1_x = screen_width / 2-205 #GameOver x
GO1_y = screen_height / 2 - 20 #GameOver y
light_grey = (239, 231, 200)
