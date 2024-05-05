import pygame, sys, os

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

def execute_python_file(file_path):
   try:
      os.system(f'python {file_path}')
   except FileNotFoundError:
      print(f"Error: The file '{file_path}' does not exist.")
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
            # Play tictactoe
            if event.pos[0]<screen_width/2:
                pygame.quit()
                execute_python_file("C:/Users/abdul/PycharmProjects/game/tictactoe/tictactoe.py")
                sys.exit()
            # Play pong
            elif event.pos[0]>screen_width/2+15:
                pygame.quit()
                execute_python_file("C:/Users/abdul/PycharmProjects/game/pong/pong.py")
                sys.exit()

#GLOBAL VARIABLES
clicked_x, clicked_y = 0, 0
screen_width, screen_height = 700, 700
line_colour = (23, 145, 135)
bg_color = (28, 170, 156)
cross_clr = (66, 66, 66)

text_font = pygame.font.Font("freesansbold.ttf", 40)
light_grey = (239, 231, 200) # text colour

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# MAIN
while True:
    handle_inputs()
    screen.fill(bg_color)
    # Draw centre line
    pygame.draw.line(screen, line_colour, (screen_width/2-15, 0), (screen_width/2-15, screen_height), 15)

    #Draw TicTacToe side
    text1 = text_font.render("TIC-TAC-TOE", False, light_grey)
    screen.blit(text1, (35, 20))

    #Horizontal Lines
    pygame.draw.line(screen, line_colour, (30, 300), (280, 300), 10)
    pygame.draw.line(screen, line_colour, (30, 400), (280, 400), 10)

    #Verical Lines
    pygame.draw.line(screen, line_colour, (110, 218), (110, 480), 10)
    pygame.draw.line(screen, line_colour, (200, 218), (200, 480), 10)

    #X in centre
    pygame.draw.line(screen, cross_clr, (125, 320), (185, 380), 10)
    pygame.draw.line(screen, cross_clr, (185, 320), (125, 380), 10)

    #Draw Pong side
    text2 = text_font.render("PONG", False, light_grey)
    screen.blit(text2, (450, 20))

    pygame.draw.line(screen, light_grey, (370, 295), (370, 395), 10)
    pygame.draw.line(screen, light_grey, (screen_width-20, 295), (screen_width-20, 395), 10)
    pygame.draw.circle(screen, light_grey, (530, 345), 10)

    pygame.display.flip()
    clock.tick(60)

