#Developer Name: Anuja,Juan,Foti
#Project Name: Turbo Pong
#Developing Date: January 19th
#Description: A game of pong with music and sound effects  (that is our challenge)

#Imports libraries
import pygame
import time
import random

#initializes pygame and pygame mixer
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

#Loads the music and picture of the ball
pygame.mixer.set_num_channels(10)
pygame.mixer.music.load("bounce.wav")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.load("menu_music.wav")
pygame.mixer.music.load("instructions_music.wav")
pygame.mixer.music.load("buzzer.wav")
pygame.mixer.music.load("youWon.wav")
pygame.mixer.music.load("youLose.wav")
pygame.mixer.music.load("youLose1.wav")
pygame.mixer.music.load("youLoseBackground.wav")
pygame.mixer.music.load("point.wav")
ballImg = pygame.image.load('Ball.png')

#Sets values for constants
DISPLAY_WIDTH=950
DISPLAY_HEIGHT=650
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(240,20,20)
GREEN=(25,160,65)
BLUE=(60,160,230)
YELLOW=(255, 211, 0)
BALL_WIDTH = 50



#Makes the game window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Turbo Pong')

#Sets up clock
clock = pygame.time.Clock()

#Takes the different values of the paddle and draws it 
def paddle(paddleX, paddleY, paddleWidth, paddleHeight, white):
    pygame.draw.rect(gameDisplay, white, [paddleX, paddleY, paddleWidth, paddleHeight])

#Takes the different values of the rectangles and draws it 
def rectangle(rectangleX, rectangleY, rectangleWidth, rectangleHeight, white):
    pygame.draw.rect(gameDisplay, white, [rectangleX, rectangleY, rectangleWidth, rectangleHeight])

#Takes the x and y coordinate of the ball and prints it 
def ball(ballX,ballY):
    gameDisplay.blit(ballImg, (ballX,ballY))

#Displays statements
def textObjects (text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#Sets up everything needed to display a statement (text, font size, x and y coordinate)
def messageDisplay(text, fontsize, placeX, placeY):
    largeText = pygame.font.Font('freesansbold.ttf', fontsize)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = (placeX, placeY)
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

#Counts and displays the score
def score(currentScore):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(currentScore), True, WHITE)
    gameDisplay.blit(text, (775,5))

#Counts and displays the lives remaining
def lives(currentLives):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Lives: " + str(currentLives), True, WHITE)
    gameDisplay.blit(text, (5,5))
    
#Tells the user that they won 
def youWon():
    
    #Displays all the text and plays the music 
    gameDisplay.fill(WHITE)
    pygame.mixer.Channel(5).play(pygame.mixer.Sound('youWon.wav'),999)
    messageDisplay('CONGRATULATIONS!!!', 75, (DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/4))
    messageDisplay('You Won', 200, (DISPLAY_WIDTH/2), 400)
    messageDisplay('Back to Main Menu', 20, 100, 625)

    #Gets the x and y coordinates of the mouse click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                #If the mouse click was on main menu, calls mainMenu and stops the music
                if y>615 and y<630:
                    if x>5 and x < 190:
                        pygame.mixer.Channel(5).stop()
                        mainMenu()
                        
#Tells the user that they lost
def youLost():
    
    #Displays all the text and plays the music
    gameDisplay.fill(WHITE)
    pygame.display.update()
    pygame.mixer.Channel(8).play(pygame.mixer.Sound('youLoseBackground.wav'),999)
    pygame.mixer.Channel(6).play(pygame.mixer.Sound('youLose.wav'))
    time.sleep(3.75)
    pygame.mixer.Channel(7).play(pygame.mixer.Sound('youLose1.wav'))
    messageDisplay('Game Over', 150, (DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
    messageDisplay('Back to Main Menu', 20, 100, 625)
    pygame.display.update()

    #Gets the x and y coordinates of the mouse click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                #If the mouse click was on main menu, calls mainMenu and stops the music
                if y>615 and y<630:
                    if x>5 and x < 190:
                        pygame.mixer.Channel(8).stop()
                        mainMenu()
                        
#Tells the user how to play and win the game
def howToPlay():
    
    #Displays all the text and plays the music
    gameDisplay.fill(WHITE)
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('instructions_music.wav'),999)    
    messageDisplay('How to Play', 100, (DISPLAY_WIDTH/2), 100)
    messageDisplay('Use the arrow keys to move ', 30, (DISPLAY_WIDTH/2), 225)
    messageDisplay('the paddle and keep the ball alive ', 30, (DISPLAY_WIDTH/2), 255)
    messageDisplay('In order to win, you need', 30, (DISPLAY_WIDTH/2), 315)
    messageDisplay('to get a score of 25 ', 30, (DISPLAY_WIDTH/2), 345)
    messageDisplay('with your 3 extra lives', 30, (DISPLAY_WIDTH/2), 375)
    messageDisplay('GOOD LUCK!', 75, (DISPLAY_WIDTH/2), 500)
    messageDisplay('Back to Main Menu', 20, 100, 625)

    #Gets the x and y coordinates of the mouse click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                #If the mouse click was on main menu, calls mainMenu and stops the music
                if y>615 and y<630:
                    if x>5 and x < 190:
                        pygame.mixer.Channel(3).stop()
                        mainMenu()
                        
#Is the main game loop                        
def gameLoop():
    
    #Sets the values of all the variables
    xVelocity = 0
    paddleX = 475
    paddleY = 625
    paddleWidth = 120
    paddleHeight = 10
    ballX = random.randrange(0,DISPLAY_WIDTH-BALL_WIDTH) 
    ballY = random.randrange(0 + BALL_WIDTH,DISPLAY_HEIGHT - DISPLAY_HEIGHT/2)
    ballVelocityX = 1.25
    ballVelocityY = -1.25
    currentScore = 0
    currentLives = 3
    waitTime = 0
    scoreCheck = False
    gameExit = False
    
    #Plays the music 
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('background.wav'),999)
    pygame.mixer.Channel(1).set_volume(0.4)

    #If user does not exit
    while gameExit ==False:
        for event in pygame.event.get():

            #If user exits, exit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Moves the paddle left or right with user input on the arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xVelocity = -2.5
                elif event.key == pygame.K_RIGHT:
                    xVelocity = 2.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xVelocity = 0

        #Keeps the paddle on the game screen
        if paddleX<=0 and xVelocity<0:
            xVelocity=0
        if paddleX + paddleWidth>=DISPLAY_WIDTH and xVelocity>0:
            xVelocity=0

        #Makes the background white
        gameDisplay.fill(BLACK)

        #Calls paddle and ball which draw the objects; allows them to move
        paddle(paddleX, paddleY, paddleWidth, paddleHeight, WHITE)
        paddleX = paddleX + xVelocity
        ball(ballX,ballY)
        ballX += ballVelocityX
        ballY += ballVelocityY

        #Sends the values of the current score and lives 
        score(currentScore)
        lives(currentLives)

        #If the ball hits the top, left and right edge of the screen, causes it to bounce with a sound effect
        if ballX <= 0 or ballX + BALL_WIDTH >= DISPLAY_WIDTH:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('bounce.wav'))
            ballVelocityX *= -1
            scoreCheck = True
        if ballY <= 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('bounce.wav'))
            ballVelocityY *= -1
            scoreCheck = True

        #If the balls hits the top of the paddle, causes it to bouce off faster with a sound effect
        if ballX>=paddleX and ballX<=paddleX+paddleWidth or ballX + BALL_WIDTH >= paddleX and ballX + BALL_WIDTH <= paddleX + paddleWidth:
            if ballY + BALL_WIDTH >= paddleY and ballY + BALL_WIDTH <= paddleY + 7:
                pygame.mixer.Channel(9).play(pygame.mixer.Sound('point.wav'))
                ballVelocityY = ballVelocityY * -1 - 0.15
                ballY -= 2
                if scoreCheck:
                    currentScore += 1
                    scoreCheck = False
                
                if ballVelocityX > 0:
                    ballVelocityX += 0.15
                else:
                    ballVelocityX -= 0.15
               
       #If the ball hits the left side of the paddle, causes the ball to bounce with sound effect and add one to the score
        if ballX+BALL_WIDTH>=paddleX and ballX + BALL_WIDTH <= paddleX + 5:
            if ballY + BALL_WIDTH>=paddleY and ballY <= paddleY+paddleHeight:
                pygame.mixer.Channel(9).play(pygame.mixer.Sound('point.wav'))
                if scoreCheck:
                    currentScore += 1
                    scoreCheck = False
                ballX -=5
                ballVelocityX = ballVelocityX * -1

        #If the ball hits the right side of the paddle, cause the ball to bounce with sound effect and add one to the score
        if ballX<=paddleX+paddleWidth and ballX >= paddleX + paddleWidth -5:
            if ballY + BALL_WIDTH >=paddleY and ballY<=paddleY+paddleHeight:
                pygame.mixer.Channel(9).play(pygame.mixer.Sound('point.wav'))
                if scoreCheck:
                    currentScore += 1
                    scoreCheck = False
                ballX += 5
                ballVelocityX = ballVelocityX * -1
                

        #If the ball goes past the paddle, resets the speed and coordinates of the ball and causes the player to lose a life with a sound effect      
        if ballY>=DISPLAY_HEIGHT+BALL_WIDTH:
                ballX = random.randrange(0,DISPLAY_WIDTH-BALL_WIDTH) 
                ballY = random.randrange(0 + BALL_WIDTH,DISPLAY_HEIGHT - DISPLAY_HEIGHT/2)
                ballVelocityX = 1.25
                ballVelocityY = -1.25
                ball(ballX,ballY)
                ballX += ballVelocityX
                ballY += ballVelocityY
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('buzzer.wav'),0,800)
                pygame.mixer.Channel(5).set_volume(0.6)
                currentLives -= 1
                time.sleep(1)

        #If the player has less than 0 lives left, stops music and calls youLost
        if currentLives==0:
            pygame.mixer.Channel(1).stop()
            time.sleep(1)
            youLost()
            
        #If the player has a score of 25, stops music and calls youWon
        if currentScore==25:
                waitTime += 2.5
                pygame.mixer.Channel(1).stop()
                if waitTime == 100:
                    youWon()
                
                
        #Updates the screen and sets clock speed
        pygame.display.update()
        clock.tick(450)

#Displays the main menu
def mainMenu():
    
    #Displays all the text and plays the music
    gameDisplay.fill(WHITE)
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('menu_music.wav'),999)
    rectangle(115,90,720,120,YELLOW)
    messageDisplay('Turbo Pong', 105, (DISPLAY_WIDTH/2), 150)
    time.sleep(0.5)
    rectangle(350,280,250,45,GREEN)
    messageDisplay('Play', 40, (DISPLAY_WIDTH/2), 300)
    time.sleep(0.5)
    rectangle(350,380,250,45,RED)
    messageDisplay('Exit', 40, (DISPLAY_WIDTH/2), 405)
    time.sleep(0.5)
    rectangle(350,480,250,45,BLUE)
    messageDisplay('How to Play', 40, (DISPLAY_WIDTH/2), 500)
    messageDisplay('Anuja Juan Foti', 20, 85, 625)
    pygame.display.update()

    #Gets the x and y values of the mouse click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                #If the mouse click was on play, calls gameLoop and stops the music                
                if y>280 and y<325 and x>350 and x < 600:
                    pygame.mixer.Channel(2).stop()
                    gameLoop()

                #If the mouse click was on quit, quits the game
                if y>380 and y<425 and x>350 and x < 600:
                    pygame.quit()
                    quit()
                    
                #If the mouse click was on how to play, calls howToPlay and stops the music
                if y>480 and y<525 and x>350 and x < 600:
                    pygame.mixer.Channel(2).stop()
                    howToPlay() 
                    
#Calls the main menu    
mainMenu()
