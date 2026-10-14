import pygame , random 


# import pygame module in this program 
import pygame, sys 
from pygame.locals import *
   
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init()
   


   
# Stores if player is jumping or not
isjump = False
   
# Force (v) up and mass m.
v = 10
m = 1
   
# Indicates pygame is running
run = True






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

image_sprite_straight = [pygame.image.load(r'C:\Users\simsa\Desktop\left\\standing_straight.png')]
straight_animation_value=0


image_sprite_apple = [pygame.image.load(r'C:\Users\simsa\Desktop\left\\apple.png')]
apple_animation_value=0  





wall = Rect(0,750,1200,600)
#(x coordinate, , y coordinate, length, how far down does it go )


score = 0
score_increment = 1










can_godown=True







def functioning_apple():

    global box
    global box2
    boxx = random.randrange(0,800)
    boxy = random.randrange(500,700)
    box_length= random.randrange(50,400)
    box_depth = boxy + 600
    box = Rect(boxx,boxy,box_length,box_depth)
    image_apple = image_sprite_apple[apple_animation_value] 
    image_apple = pygame.transform.scale(image_apple, (50, 50))  




    global box2x
    global box2y
    global box2
    box2x = random.randrange(boxx -400,boxx +400)
    box2y = random.randrange(boxy -300,boxy -150)
    box2_length = random.randrange(box_length +100 ,box_length +200)
    box2_depth = random.randrange(50, 100)
    box2 = Rect(box2x,box2y,box2_length,box2_depth)

    global applex 
    global appley
    applex =  random.randrange(box2x -250,box2x +250)
    appley = random.randrange(box2y -300,box2y -200)

 
    if box2x> 850 or box2x < 50 or box2y > 1100 or box2y < 50:
        functioning_apple()
    if applex > 850 or applex < 50 or appley > 1100 or appley < 50:
        functioning_apple()
       

    
    window.blit(image_apple, (applex, appley))
    pygame.draw.rect(window, (255,   80,   150),box2)
    pygame.draw.rect(window, (0,   255,   0),wall)
    pygame.draw.rect(window, (255,   0,   0),box)

    
    pygame.display.flip()


functioning_apple()



while run:
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (0, 0, 255))
    
    if playery < (appley + 40):
        if ((playerx > applex
            and playerx< (applex + 40))
            or ((playerx + 50) >applex
            and (playerx + 40) < (applex + 50))):
                    score += score_increment
                    functioning_apple()
                   



    image_straight = image_sprite_straight[straight_animation_value] 
    image_straight = pygame.transform.scale(image_straight, (90, 90))  
    image_right = image_sprite_right[right_animation_value] 
    image_left = image_sprite_left[left_animation_value] 
    image_right = pygame.transform.scale(image_right, (90, 90))  
    image_left = pygame.transform.scale(image_left, (90, 90)) 
    image_apple = image_sprite_apple[apple_animation_value] 
    image_apple = pygame.transform.scale(image_apple, (50, 50))  



    image1 = image_left.get_rect(topleft=( playerx,playery))
    image2 = image_right.get_rect(topleft=( playerx,playery))
    image3 = image_straight.get_rect(topleft=( playerx,playery))



    clock.tick(30)
    
    
    window.blit(image_straight, (playerx, playery))


    def environment():
        window.blit(image_apple, (applex, appley))
        pygame.draw.rect(window, (255,   80,   150),box2)
        pygame.draw.rect(window, (0,   255,   0),wall)
        pygame.draw.rect(window, (255,   0,   0),box)
        window.blit(score_text, (10, 10))
        pygame.display.flip()


    environment()



    
    collide1 = pygame.Rect.colliderect(wall, image3 ) or pygame.Rect.colliderect(box, image3 ) or pygame.Rect.colliderect(box2, image3 )

    
    
    if collide1:
        can_godown = False
    else:can_godown=True
    



    
    


    
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get():

        
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT:
            
            # it will make exit the while loop
            run = False
    # stores keys pressed
        keys = pygame.key.get_pressed()
    if can_godown:
        if keys[pygame.K_s] and playery < windowheight - 100:
            window.fill((255,255,255))
            window.blit(image_straight, (playerx, playery))
            environment()
            playery += velocity
    if can_godown == True :
        if keys[pygame.K_w] and playery > 0:
            window.fill((255,255,255))
            window.blit(image_straight, (playerx, playery))
            environment()
            playery -= velocity 
    if keys[pygame.K_a] and playerx >0 :
        window.fill((255,255,255))
        window.blit(image_left, (playerx, playery))
        environment()
        left_animation_value +=1
        playerx -= velocity 
    if keys[pygame.K_d] and playerx < windowbreadth - 100:
        window.fill((255,255,255))
        window.blit(image_right, (playerx, playery))
        environment()
        right_animation_value += 1
        playerx += velocity
        
    if isjump == False:

        # if space bar is pressed
        if keys[pygame.K_SPACE]:
                
            # make isjump equal to True
            isjump = True
            
    if isjump :
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2. 

        F =(1 / 2)*m*(v**2)
        # change in the y co-ordinate
        
        if not can_godown:

            environment()

            isjump = False 
            m = 1
            v = 10
            if keys[pygame.K_SPACE]:
                F =(1 / 2)*m*(v**2)
                playery-= F
                isjump = False 
                m = 1
                v = 10



        

        if can_godown:
            if F > -128:
                playery-= F

                environment()


            
            if keys[pygame.K_s] and playery < windowheight - 100:
                
                environment()
                playery += velocity

        if can_godown == False:
            if keys[pygame.K_w] and playery > 0:
                environment()
                playery -= velocity 
        if keys[pygame.K_a] and playerx >0 :
            window.fill((255,255,255))
            window.blit(image_left, (playerx, playery))
            environment()
            left_animation_value +=1
            playerx -= velocity 
        if keys[pygame.K_d] and playerx < windowbreadth - 100:
            window.fill((255,255,255))
            window.blit(image_right, (playerx, playery))
            environment()
            right_animation_value += 1
            playerx += velocity
        
        # decreasing velocity while going up and become negative while coming down
        v = v-1
        
        # object reached its maximum height
        if v<0:
            
            # negative sign is added to counter negative velocity
            m =-1
        # objected reaches its original state
        '''
        if v ==-11 :

            # making isjump equal to false 
            isjump = False

    
            # setting original values to v and m
            v = 10
            m = 1
            '''

    if can_godown and not isjump:
        playery +=10 
        window.fill((255,255,255))
        window.blit(image_straight, (playerx, playery))
        environment()      
    if right_animation_value >= len(image_sprite_right):
            right_animation_value = 0  
    if left_animation_value >= len(image_sprite_left):
            left_animation_value = 0 
    # creates time delay of 10ms



    # it refreshes the window
    pygame.display.update() 
# closes the pygame window  


pygame.quit()
sys.exit(0)