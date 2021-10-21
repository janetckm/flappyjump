import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))

BACKGROUND_IMAGE = pygame.image.load('background.jpg')


# character
BIRD_IMAGE = pygame.image.load('car.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))
# character end 


OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)
OBSTACLE_X_CHANGE = -4
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 535 - height - 150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, -bottom_obstacle_height))
#obstacle end

running = True
while running:
   
  SCREEN.fill((0, 0, 0))
   
  SCREEN.blit(BACKGROUND_IMAGE,(0, 0))
   
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    #Spacebar control up / down
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
         bird_y_change = -6
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE:
        bird_y_change = 3
    #spacebar control END

  #move bird vertically
  bird_y += bird_y_change
  
  #boundary of screen
  if bird_y <= 0:
    bird_y = 0
  if bird_y >= 550:
    bird_y = 550

  #move obstacle
  obstacle_x += OBSTACLE_X_CHANGE
  if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        
  #display obstacle
  display_obstacle(OBSTACLE_HEIGHT)
  
  #display bird 
  display_bird(bird_x, bird_y)
  
  #display game 
  pygame.display.update()

pygame.QUIT()
