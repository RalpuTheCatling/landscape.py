import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 0
circle_y = 0
math_x = 1
circ_colour = [255,255,0]
cloud_x = 200
cloud_y = 200
cloud_2_x = 400
cloud_2_y = 100
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    #make it so that sun position changes sky
    screen.fill((0, math_x*(120-(circle_y/4)), math_x*(240-(circle_y/2))))  # always the first drawing command
    #sun/moon movement
    circle_x += 2
    
    math_f=circle_x-320
    #sun/moon follows parabola (also keep in mind that it is flipped)
    # y = 1/365x^2 + 60
    circle_y =1/365*(math_f*math_f)+60
    #if sun/moon is off screen
    if circle_x> WIDTH+50:
        #tp to other side of screen
        circle_x=-50
        #switches between sun and moon
        if math_x == 1:
            math_x = 0
            circ_colour = [255,255,255]
        elif math_x == 0:
            math_x = 1
            circ_colour = [255,255,0]

    #sun/moon
    pygame.draw.circle(screen, (circ_colour),(circle_x,circle_y),50)
    
    #super far mountains
    pygame.draw.polygon(screen,(29,4,5),((160,480),(300,20),(400,480)))
    pygame.draw.polygon(screen,(128,22,42),((0,480),(180,80),(240,480)))
    pygame.draw.polygon(screen,(128,39,19),((0,480),(120,100),(170,480)))
    pygame.draw.polygon(screen,(100,7,5),((480,480),(500,150),(600,480)))
    pygame.draw.polygon(screen,(90,22,0),((0,480),(10,200),(150,480)))
    pygame.draw.polygon(screen,(120,45,30),((680,480),(600,200),(500,480)))
    pygame.draw.polygon(screen,(40,17,19),((320,480),(400,40),(480,480)))

    #cloud 2
    pygame.draw.circle(screen, (230,230,230), (cloud_2_x,cloud_2_y),40)
    pygame.draw.circle(screen, (230,230,230), (cloud_2_x-20,cloud_2_y+20),30)
    pygame.draw.circle(screen, (230,230,230), (cloud_2_x+20,cloud_2_y+20),30)  
    
    #far mountains 
    pygame.draw.polygon(screen,(250,60,13),((300,480),(380,100),(400,480))) 
    pygame.draw.polygon(screen,(50,15,7),((480,480),(580,100),(680,480)))  
    pygame.draw.polygon(screen,(128,0,0),((100,480),(150,120),(250,350),(300,480))) 
    
    #cloud 1
    pygame.draw.circle(screen, (245,240,250), (cloud_x,cloud_y),70)
    pygame.draw.circle(screen, (245,240,250), (cloud_x-50,cloud_y+20),60)
    pygame.draw.circle(screen, (245,240,250), (cloud_x+50,cloud_y+20),60)
    
    #close mountains
    pygame.draw.polygon(screen,(165,42,42),((140,480),(180,160),(210,280),(225,248),(240,480)))
    pygame.draw.polygon(screen,(139,69,19),((0,480),(120,160),(170,480)))
    pygame.draw.polygon(screen,(222,184,135),((480,480),(500,300),(600,480)))
    pygame.draw.polygon(screen,(140,22,0),((0,480),(0,220),(150,480)))
    pygame.draw.polygon(screen,(120,45,30),((680,480),(600,200),(500,480)))
    pygame.draw.polygon(screen,(160,45,30),((500,480),(467, 259),(400,480)))
    467, 259

    #hills
    pygame.draw.circle(screen, (75,100,25),(600,480),100)
    pygame.draw.circle(screen, (75,120,30),(100,480),150)
    pygame.draw.circle(screen, (140,255,150),(160,550),200)
    pygame.draw.circle(screen, (140,255,100),(480,550),200)
    pygame.draw.circle(screen, (75,255,25),(320,480),200)

    #house
    pygame.draw.rect(screen, (255,30,30),(200,250,240,180))
    pygame.draw.polygon(screen, (240,120,70), ((320, 100), (160, 250), (480, 250)))
    pygame.draw.rect(screen,(128,40,60),(295,340,50,90))
    pygame.draw.circle(screen, (0,0,0),(335,380),5)
    
    #cloud movement
    cloud_x += 4.5
    cloud_2_x +=3

    #teleportation for clouds
    if cloud_x-110 > WIDTH:
            cloud_x = -110
    if cloud_2_x-50 > WIDTH:
        cloud_2_x = -50
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
