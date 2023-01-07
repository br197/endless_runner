import pygame
import random #r enemy spawning, random generation
pygame.init() #initialize pygame modules
import time
from os import path
from pygame import mixer
mixer.init()

#------GAME CONSTANTS------
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
cyan = (0, 100, 100)
pink = (255, 0 ,255)
red = (255, 0 ,0)
sky = (135, 206, 235)
cerise = (222, 49, 99)
orange = (245, 176,65)
yellow = (241, 196, 15)
green_light = (88, 214, 141)
indigo = (75, 0 , 130)
violet = (142, 68, 173)
    #screen dimensions
WIDTH = 450
HEIGHT = 300

#---------files------
high_score_file = "highscore.txt"
mixer.music.load("stranger_things.wav")
pygame.mixer.music.play()

#--------GAME VARIABLES-------

score = 0
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1
obstacles = [450, 550, 650] #positions obstacles spawn in at
obstacle_speed = 2
active = False
intro = False
end = False
score_file = 0
count = 0

screen = pygame.display.set_mode([WIDTH, HEIGHT]) #set game window dimensions
pygame.display.set_caption('Jumping Dots') #gives title of game window

background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
intro_text = pygame.font.Font('freesansbold.ttf', 50)
end_text = pygame.font.Font('freesansbold.ttf', 25)
timer = pygame.time.Clock() #tracks time

running = True

while running: #main game loop
    timer.tick(fps)
    screen.fill(background)
    


    while not intro:
        title = intro_text.render('Jumping Dots', True, white, black)
        instruc = font.render('press q to play', True, white, black)
        screen.blit(title, (50, 100))
        screen.blit(instruc, (50,200))
        pygame.display.update()
        timer.tick(15)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    intro = True
    
    screen.fill(background)
        

    if not active:
        background = black
        end = False
        player_x = 0
        x_change = 0
        instruction_text1 = font.render(f'Hit Space Bar to Start', True, white, black) #need this before draw on screen
        instruction_text2 = font.render(f'Use D to move RIGHT', True, white, black)
        instruction_text3 = font.render(f'Use A to move LEFT', True, white, black)
        screen.blit(instruction_text1, (50,50)) #draw something on screen
        screen.blit(instruction_text2, (50,70))
        screen.blit(instruction_text3, (50,90))
    

    score_text = font.render(f'Score: {score}', True, white, black) #need this before draw on screen
    screen.blit(score_text, (0,0)) #draw something on screen
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, cyan, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, pink, [obstacles[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #allows you to exit game
            running = False
            
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                pygame.display.update()
                obstacles = [450, 550, 650]
                score = 0
                player_x = 0
                count = 0
                player_y = 200
                active = True
                
            

        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_SPACE and y_change == 0: #jump
                y_change = 17
                
            if event.key == pygame.K_d:
                    x_change = 2
            if event.key == pygame.K_a:
                    x_change = -3
            if event.key == pygame.KEYUP:
                if event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_a:
                    x_change = 0
        
    for i in range (len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed #move obstacles toward player
            if player.x - obstacles[i] > 30:
                score += 1
                if score % 10 == 0:
                    obstacle_speed += .25
                    count += 1
                    if count == 1:
                        background = cerise
                    elif count == 2:
                        background = orange
                    elif count == 3:
                        background = yellow
                    elif count == 4:
                        background = green_light
                    elif count == 5:
                        background = sky
                    elif count == 6:
                        background = indigo
                    else:
                        background = violet
                 

                        
                obstacles[i] = random.randint(470, 570)
        
            
            if abs(obstacles[1]-obstacles[0]) <= 90:
                obstacles[1] += 50
            if abs(obstacles[1]-obstacles[2]) <= 90:
                obstacles[2] += 50
            if abs(obstacles[0]-obstacles[2]) <= 90:
                obstacles[0] += 50
                
    
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2): #player collides with obstacle
                while not end:
                    title = font.render('Want to Play Again? (press y), press h for score', True, white, black)
                    screen.blit(title, (50, 100))
                    pygame.display.update()
                    timer.tick(15)
                    if score > score_file:
                        score_file = score
                        title = end_text.render(f"New Highscore!: {score_file}", True, white, black)
                        screen.blit(title,(50,50))
                        pygame.display.update()
                        timer.tick(15)
                        with open("highscore.txt", "w") as f:
                            f.write(str(score_file))            

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_y:
                                end = True
                            if event.key == pygame.K_h:
                                with open("highscore.txt", "r") as f:
                                    try:
                                        score_file = int(f.read()) #checks if number in file
                                    except:
                                        score_file = 0 #nothing in file
                                if score <= score_file:
                                    screen.fill(black)
                                    title = end_text.render(f"Highscore: {score_file}", True, white, black)
                                    screen.blit(title, (50,50))
      
                #time.sleep(1)
                screen.fill(background)
                active = False
            
            
            

    if 0 <= player_x <= 430:
        player_x += x_change
    
    if player_x < 0:
        player_x = 0
    
    if player_x > 430:
        player_x = 430

    if y_change > 0 or player_y < 200: #progressive fall
        player_y -= y_change
        y_change -= gravity
    if player_y == 200 and y_change < 0:
        y_change = 0

    if player_y >= 200:
        player_y = 200
    
    pygame.display.flip() #updates screen

pygame.quit()

