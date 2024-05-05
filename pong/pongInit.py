# SCREEN
import pygame

pygame.init()
pygame.font.init()

screen_width = 1280
screen_height = 720
# bg_color = pygame.Color('grey12')
# light_grey = (200, 200, 200)

bg_color = (28, 170, 156)
light_grey = (239, 231, 200)

# BALL
speed_up_num = 10000

ball_size = 30

ball_x = screen_width / 2 - (ball_size / 2)
ball_y = screen_height / 2 - (ball_size / 2)

ball_speed_x = 8
ball_speed_y = 8


# PADDLES
paddle_width = 15
paddle_height = 140

r_paddle_x = screen_width - 40
r_paddle_y = screen_height / 2 - 70

l_paddle_x = 20
l_paddle_y = screen_height / 2 - 70

l_player_speed = 0
r_player_speed = 0


# CENTRE LINE
line_width = 3
line_height = screen_height

line_x = screen_width / 2 - 2
line_y = 0


# TEXT
l_score = 0
r_score = 0

l_score_x = screen_width / 2 + 5
r_score_x = screen_width / 2 - 23
l_score_y = screen_height / 2
r_score_y = screen_height / 2

#GameOver text
GO1_x = screen_width / 2-205
GO1_y = 50

#Start Screen text

#L-player
SS1_x = 150
SS1_y = screen_height - 70
#R-player
SS2_x = line_x+line_width+140
SS2_y = screen_height - 70
#Top title
SS3_x = 443
SS3_y = 40

score_font = pygame.font.Font("freesansbold.ttf", 32)
text_font = pygame.font.Font("freesansbold.ttf", 64)
start_screen_font = pygame.font.Font("freesansbold.ttf", 36)


# GAMEOVER SCREEN
game_over_score = 3
display_game_over = False
winning_player = 'LEFT'

# START SCREEN
display_start_screen = True

# SOUND
pong_sound = pygame.mixer.Sound("C:/Users/abdul/PycharmProjects/game/pong/audio/pong.ogg")
score_sound = pygame.mixer.Sound("C:/Users/abdul/PycharmProjects/game/pong/audio/score.ogg")
win_sound = pygame.mixer.Sound("C:/Users/abdul/PycharmProjects/game/pong/audio/win.wav")
