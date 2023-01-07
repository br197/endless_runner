import pygame
import random #r enemy spawning, random generation
pygame.init() #initialize pygame modules

#------GAME CONSTANTS------
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
cyan = (0, 100, 100)
pink = (255, 0 ,255)
red = (255, 0 ,0)
    #screen dimensions
WIDTH = 450
HEIGHT = 300

#--------GAME VARIABLES-------

score = 0
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1
obstacles = [300, 450, 600] #positions obstacles spawn in at
obstacle_speed = 2
active = False

screen = pygame.display.set_mode([WIDTH, HEIGHT]) #set game window dimensions
pygame.display.set_caption('Jumping Dots') #gives title of game window

background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock() #tracks time

running = True

while running: #main game loop
    timer.tick(fps)
    screen.fill(background)

    if not active:
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
                obstacles = [300, 450, 600]
                score = 0
                player_x = 50
                player_y = 200
                active = True

        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_SPACE and y_change == 0: #jump
                y_change = 15
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
            if obstacles[i]< -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
    
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2): #player collides with obstacle
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

    if player_y > 200:
        player_y = 200
    
    pygame.display.flip() #updates screen

pygame.quit()

