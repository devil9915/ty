import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600
def thing(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    
    

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
red2 = (200,0,0)
green=(0,255,0)
green2=(0,200,0)
blue=(0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('car game')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
def quitgame():
    pygame.quit()
    quit()
def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text =  font.render("Score: +"+str(count),True,black)
    gameDisplay.blit(text,(0,0))
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
def message_display(text): 
    largeText= pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def crash():
    message_display('you crashed')
def button(msg,x,y,w,h,ic,ac,action=None):
    click = pygame.mouse.get_pressed()
    print (click)
    mouse = pygame.mouse.get_pos()
    if x+w > mouse[0]>x and y+h >mouse[1]>y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    
   
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText= pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect = text_objects("Car game",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("Race!",150,450,100,50,green2,green,game_loop)
        button("Exit",550,450,100,50,red2,red,quitgame)


        pygame.display.update()
        clock.tick(15)


        
def game_loop():
        
    x=(display_width*0.45)
    y=(display_height*0.64)

    x_change=0
    y_change=0
    thing_startx=random.randrange(0,display_width-150)
    thing_starty=-600
    thing_width=100
    thing_height=100
    thing_speed=7
    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                elif event.key == pygame.K_RIGHT:
                    x_change = 8 
                #elif event.type == pygame.KEYDOWN:
                 #   if event.key == pygame.K_UP:
                  #      y_change = -5
                #elif event.type == pygame.KEYDOWN:
                 #   if event.key == pygame.K_DOWN:
                  #      y_change = +5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0
               
        x +=x_change
        y +=y_change
        gameDisplay.fill(white) 
        #thingx,thingy,thingw,thingh,color
        thing(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x>display_width-140 or x<-65:
            crash()
        if thing_starty > display_height:
            thing_starty = 0-thing_height
            thing_startx = random.randrange(0,display_width-150)
            dodged+=1
            thing_speed +=.5
        if y+84.5<thing_starty+thing_height:
            
            if x+70>thing_startx and x+70<thing_startx+thing_width or x+130> thing_startx and x+130<thing_startx+thing_width:
                crash()
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit() 
quit()
 
