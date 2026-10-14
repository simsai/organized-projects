import pygame , sys 
from pygame.locals import *




pygame.init()

window = pygame.display.set_mode((600, 600))
 
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
 
 
# Creating a new rect for first object
player_rect = Rect(200, 500, 50, 50)
 
# Creating a new rect for second object
player_rect2 = Rect(200, 0, 50, 50)
 
 
# Creating a boolean variable that
# we will use to run the while loop
run = True
 
# Speed for the objects
speed_a = 8
speed_b = -7
 
# Creating an infinite loop
# to run our game
while run:
 
    # Setting the framerate to 60fps
    clock.tick(60)
 
    # Adding speed in player rects
    player_rect.bottom += speed_a
    player_rect2.top += speed_b
 
    # Checking if player is colliding
    # with platform or not using the
    # colliderect() method.
    # It will return a boolean value
    collide = pygame.Rect.colliderect(player_rect,
                                      player_rect2)
 
    # If the objects are colliding
    # then changing the speed direction
    if collide:
        speed_a *= -1
        speed_b *= -1
 
    # Changing the direction if the objects
    # goes outside the window
    if player_rect.top<0 or player_rect.bottom > 600:
        speed_a *= -1
    if player_rect2.bottom > 600 or player_rect2.top<0:
        speed_b *= -1
     
    # Drawing player rect
    pygame.draw.rect(window, (0,   255,   0),
                     player_rect)
    # Drawing player rect2
    pygame.draw.rect(window, (0,   0,   255),
                     player_rect2)
 
    # Updating the display surface
    pygame.display.update()
 
    # Filling the window with white color
    window.fill((255, 255, 255))







"""
windowheight = 900
windowbreadth = 1200
window = pygame.display.set_mode((windowbreadth, windowheight))
pygame.display.set_caption('Player Movement')

#image = pygame.image.load(r'C:\Users\simsa\Desktop\\Playerspriteusedinpygame21.png').convert()

playerx = 200
playery = 200
velocity = 5
player_mass = 1

right_animation_value=0
left_animation_value=0

clock = pygame.time.Clock()

done = False
moveRight = False 
moveLeft = False 
moveUp = False 
moveDown = False 
jump = False





image_sprite_right = [pygame.image.load(r'C:\Users\simsa\Desktop\right\\1.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\2.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\3.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\4.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\5.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\6.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\7.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\8.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\9.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\right\\10.png'),
]


image_sprite_left = [pygame.image.load(r'C:\Users\simsa\Desktop\left\\1.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\2.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\3.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\4.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\5.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\6.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\9.png'),
                pygame.image.load(r'C:\Users\simsa\Desktop\left\\10.png'),
]




while not done:
    clock.tick(30)
    window.fill((255,255,255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # Change the keyboard variables.

            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
        else:
            pass
        


    




        if moveDown and playery < windowheight - 100:
            
            playery += velocity
        if moveUp and playery > 0:
            
            playery -= velocity
        if moveLeft and playerx > 0:
            window.fill((255, 255, 255))
            window.blit(image_left, (playerx, playery))
            pygame.display.flip()
            left_animation_value +=1
            playerx -= velocity
        if moveRight and playerx < windowbreadth - 100:
            
            window.fill((255, 255, 255))
            window.blit(image_right, (playerx, playery))
            pygame.display.flip()
            right_animation_value += 1
            playerx += velocity  


        if right_animation_value >= len(image_sprite_right):
            right_animation_value = 0  
        if left_animation_value >= len(image_sprite_left):
            left_animation_value = 0  
        image_right = image_sprite_right[right_animation_value] 
        image_left = image_sprite_left[left_animation_value] 
        image_right = pygame.transform.scale(image_right, (90, 90))  
        image_left = pygame.transform.scale(image_left, (90, 90))  


    
    
    
    
    pygame.display.update()
pygame.quit()
sys.exit(0)

"""