import pygame
from pygame import mixer # adding music to it


import random
import math
pygame.init()



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Momo jump")
# background mucic 
mixer.music.load('')
mixer.music.play(-1)# play continuously as its in loop

MomoImag = pygame.image.load('pygame\GAME\dog.png')
MomoX = 370
MomoY = 480
MomoX_change = 0
# randomly show the bone
boneImag = []
boneX = []
boneY = []
boneX_change = []
boneY_change = []
num_of_bone = 3
for i in range (num_of_bone):
   boneImag.append(pygame.image.load('pygame\GAME\moo.png'))
   boneX.append(random.randint(0, 800))
   boneY.append(random.randint(50, 150))
   boneX_change.append(4)
   boneY_change.append(40) 

ballImag = pygame.image.load('pygame\GAME\poo .png')
ballX = 0
ballY = 480
ballX_change = 0
ballY_change = 1
ball_state = "ready" # you cant see ball on the screen

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("score ;" + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = font.render("GAME OVER ", True, (255,255,255))
    screen.blit(over_text, (200, 250))
def Momo (x, y): 
    screen.blit(MomoImag, (x, y))


def bone (x, y, i):
    screen.blit(boneImag[i], (x, y))

def fire_ball(x, y):
  global ball_state
  ball_state = "fire" # ball is currently in motion
  screen.blit(ballImag, (x + 16, y + 10))
 
def isCollision(boneX,boneY,ballX,ballY):
  distance = math.sqrt((math.pow(boneX - ballX, 2)) + (math.pow(boneY - ballY, 2)))  
  if distance < 27:
    return True
  else:
    return False
#game loop
running = True
while running:


    screen.fill('purple')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MomoX_change = -1
            if event.key == pygame.K_RIGHT:
                MomoX_change = 1
            if event.key == pygame.K_SPACE:
              if ball_state is 'ready':
                ball_Sound = mixer.Sound('pygame\GAME\laser.wav')
                ball_Sound.play()
                ballX = MomoX
                fire_ball(ballX, ballY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                MomoX_change = 0
              

    MomoX += MomoX_change
    if MomoX <= 0:
      MomoX = 0
    elif MomoX >= 736:
      MomoX = 736      
    
    

    for i in range(num_of_bone): 
      # game over 
        if boneY[i] > 440:
          for j  in range(num_of_bone):
            boneY[j] = 2000
          game_over_text()
          break
              
        boneX[i] += boneX_change[i]
        if boneX[i] <= 0:
           boneX_change[i] = 0.3
           boneY[i] += boneY_change[i]  
        elif boneX[i] >= 736:
           boneX_change[i] = -0.1
           boneY[i] += boneY_change[i]
        collision = isCollision(boneX[i], boneY[i], ballX, ballY)
        if collision:
           clash_Sound = mixer.Sound('pygame\GAME\explosion.wav')
           clash_Sound.play()
           ballY = 480
           ball_state = "ready"
           score_value += 1
          
           boneX[i] = random.randint(50, 800)
           boneY[i] = random.randint(50, 150)
        
        bone(boneX[i], boneY[i], i)

      # ball movement

    if ballY <= 0:
      ballY = 480
      ball_state = "ready"

    if ball_state is "fire":
      fire_ball(ballX, ballY)
      ballY -= ballY_change
    

    Momo(MomoX, MomoY)
    show_score(textX, textY)

    pygame.display.update()
pygame.quit()