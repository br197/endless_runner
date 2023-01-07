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
fps = 60
y_change = 0
font = pygame.font.Font('freesansbold.ttf', 16)
intro_text = pygame.font.Font('freesansbold.ttf', 50)
end_text = pygame.font.Font('freesansbold.ttf', 25)
timer = pygame.time.Clock() #tracks time

#---------files------
high_score_file = "highscore.txt"
mixer.music.load("stranger_things.wav")
tree_image = pygame.image.load("tree.png")
tree = pygame.transform.scale(tree_image,  (30, 50))
sun_image = pygame.image.load("sun.png")
sun = pygame.transform.scale(sun_image, (50, 50))

pygame.mixer.music.play()

#-----player----------
gravity = 1
score_file = 0

#------initial surface------
WIDTH = 450
HEIGHT = 300
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Jumping Dots') #gives title of game window

def collision(): 
    if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2): #player collides with obstacle
        screen.fill(background)
        active()

def random_gen():
    player_x = 0
    obstacles = [450, 550, 650]
    for i in range (len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed #move obstacles toward player
            if player.x - obstacles[i] > 30:
                score += 1
                if score % 7 == 0:
                    obstacle_speed += .25
                    count += 1
                    if count == 1:
                        background = sky
                obstacles[i] = random.randint(470, 570)
        
            
            if abs(obstacles[1]-obstacles[0]) <= 90:
                obstacles[1] += 50
            if abs(obstacles[1]-obstacles[2]) <= 90:
                obstacles[2] += 50
            if abs(obstacles[0]-obstacles[2]) <= 90:
                obstacles[0] += 50
            
def active():
    player_x = 0
    player_y = 200
    score = 0
    obstacles = [450, 550, 650]
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


def draw_window_intro():
    screen.fill(black)
    title = intro_text.render('Jumping Dots', True, white, black)
    instruc = font.render('press q to play', True, white, black)
    screen.blit(title, (50, 100))
    screen.blit(instruc, (50,200))
    timer.tick(15)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    screen.fill(black)
                    active()
                    
 

def main():
    x_change = 0
    count = 0
    obstacle_speed = 2

    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #allows you to exit game
                running = False
                pygame.quit()
                quit()
            
            #redo spacebar

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

        draw_window_intro()
        
    main()
    


if __name__ == "__main__":
    main()