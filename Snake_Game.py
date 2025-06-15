# Importing pygame for game functionalities, importing sys to exit game, and importing random to randomize positions
import pygame
from pygame.locals import*
import sys
import random

# making my colors
colorPINK = (255, 200, 200)
colorYELLOW = (255, 255, 0)
colorGREEN = (0, 255, 0)

# Making a score variable and setting it to zero
Score = 0


# Making my bools for my while function
Running = True
playing = None

# getting the clock
clock = pygame.time.Clock()


# initializing pygame
pygame.init()

# Screen measurements
screensize = pygame.display.set_mode((600,600),0,32)

# Bg color pink
screensize.fill(colorPINK)

# Caption
pygame.display.set_caption('Snake_Game')


"""
# Creating the snake as a sprite function
snake = pygame.sprite.Sprite()
snake.rect = pygame.Rect(300, 400, 18, 20)
snake.speed = 1
snake_grow = pygame.Rect(0,0,18,20)
"""

# main direction the snake moves
direction = 'Right'


# class SNAKE to create snake foundation and to make it sprite
class SNAKE(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colorYELLOW)
        pygame.draw.rect(self.image,color,pygame.Rect(height, width, x, y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)




# snake list to store all the snake rects
snakes = [SNAKE(colorYELLOW,18,20, 300, 400), SNAKE(colorYELLOW,18,20,300,360)]
# Adding the snake to a group
snake = pygame.sprite.Group()
for obj in snakes:
    snake.add(obj)


# Creating the apple's rect (as a sprite to check for collision later on) and adding the apple image and its cre
Size = pygame.sprite.Sprite()
Size.rect = pygame.Rect(200,170, 18, 18)
image = pygame.image.load('green-apple-transparent-background-free-png.webp')
IMAGE = pygame.transform.scale(image, (18, 18))

# Creating the Play again button
One_font = pygame.font.SysFont('Comic Sans', 60)
again = One_font.render('Play Again', False, colorPINK, colorGREEN)
P_again = pygame.Rect(160, 280, 400, 400)

# Creating the reset function that resets the score and snakes
def reset_game():
    global snakes, Score
    Score = 0
    snakes = [SNAKE(colorYELLOW, 18, 20, 300, 400), SNAKE(colorYELLOW, 18, 20, 300, 360)]
    Size.rect.x = random.randint(2, 550)

# Update game
pygame.display.update()


while Running:
    # run event
    for event in pygame.event.get():
        # if the player clicks the red 'x', it is considered a quit game and quits game
        if event.type == QUIT:
            Running = False
            pygame.quit()
            sys.exit()
        # if the player clicks the e or the escape button, it is considered a quit game and quit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # if the player touvh the buttons with the mouse playing is true so it starts the main game
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Splay.collidepoint(event.pos):
                playing = True
            if P_again.collidepoint(event.pos):
                playing = True
                reset_game()

    if playing is None:
        # making first text 'Snake game'
        screensize.fill(colorPINK)
        firstFont = pygame.font.SysFont('Comic Sans', 50)
        Snake = firstFont.render('Snake Game', True, colorGREEN, colorPINK)
        screensize.blit(Snake, (150, 70))

        # Adding the head image to screen
        size = pygame.Rect(210,170, 150, 100)
        # First image variable and second image variable
        FimageV = pygame.image.load('194210.png')
        SimageV = pygame.transform.scale(FimageV, (150,100))
        screensize.blit(SimageV, size)

        # Making the play button
        play = firstFont.render("PLAY", True, colorPINK, colorGREEN)
        Splay = pygame.Rect(232, 350, 300, 300)
        screensize.blit(play, Splay)

    if playing is True:
         # if arrow key left is pressed and direction is not right, move the object left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'Right':
                direction = 'Left'
                # if arrow key right is pressed and direction is not left, move the objevct right
            if event.key == pygame.K_RIGHT and direction != 'Left':
                direction = 'Right'

            # If arrow key up is pressed and direction is not down, move the object up
            if event.key == pygame.K_UP and direction != 'Down':
                direction = 'Up'

                # if arrow key down is pressed and direction is not up, move the object down
            if event.key == pygame.K_DOWN and direction != 'Up':
                direction = 'Down'

        # this changes the position of the next rect based on the position the rect before it was
        for i in range(len(snakes)-1,0,-1):
            snakes[i].rect.topleft = snakes[i-1].rect.topleft

        # if direction is left move the snake head left 20
        if direction == 'Left':
            snakes[0].rect.x -= 20
        # if direction is right move the snake head right 20
        if direction == 'Right':
            snakes[0].rect.x += 20
        # if direction is up move snake head up 20
        if direction == 'Up':
            snakes[0].rect.y -= 20
        # if direction is down move the snake head down 20
        if direction == 'Down':
            snakes[0].rect.y += 20



        # Check for collision between the snake and the apple
        # using collide_rect
        # if a collision is detected, the apple is relocated
        # by changing its x coordinates
        # it also adds a new rect (body wtv) to the snake list
        if pygame.sprite.collide_rect(snakes[0], Size):
            Score += 1
            Size.rect.x = random.randint(2, 550)
            last = snakes[-1]
            snake2 = SNAKE(colorYELLOW, 18, 20,last.rect.x,last.rect.y)
            snakes.append(snake2)

        # makes the apple distance(run away) from the snake when it collides with the snake body
        for snak in snakes:
            if pygame.sprite.collide_rect(snak, Size):
                Size.rect.x -= 6
                Size.rect.y -= 6

        # makes the user died when it collides with itself
        #if pygame.sprite.collide_rect(snak):
            pass


            
        # check to see if we collide with the right screen end
        # if it does, we move snake back a little
        # also ends game
        if snakes[0].rect.x > 580:
            snakes[0].rect.x = 560
            playing = False
        # check to see if we collide with the left screen end
        if snakes[0].rect.x < 1:
            snakes[0].rect.x = 2
            playing = False
        # check to see if we collide with the bottom of the screen
        if snakes[0].rect.y > 580:
            snakes[0].rect.y = 559
            playing = False
        # check to see if we collide with the left screen end
        if snakes[0].rect.y < 1:
            snakes[0].rect.y = 2
            playing = False





        # Fill screen with pink
        screensize.fill(colorPINK)

        # Create the Score text to show player score
        SecondFont = pygame.font.SysFont('Comic Sans', 30)
        SCORE = SecondFont.render(f'Score:{Score}',True, colorGREEN, colorPINK)
        screensize.blit(SCORE, (10, 10))


        # drawing/bliting the snake on screen
        for sna in snakes:
            screensize.blit(sna.image, sna.rect)



        # Create the apple
        screensize.blit(IMAGE, Size.rect)
    # makes a whole new screen
    if playing is False:
        screensize.fill(colorPINK)

        # Creating the you lose
        font = pygame.font.SysFont('Comic Sans', 100)
        lose = font.render('You Lose', False, colorGREEN, colorPINK)
        screensize.blit(lose, (90, 110))

        # bliting/drawing the play again button on screen
        screensize.blit(again,P_again)
    # updating screen
    pygame.display.update()
    # Making the game go 60 frames per second
    clock.tick(10)




