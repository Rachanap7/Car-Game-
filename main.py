import pygame
import time
import random
import sqlite3

pygame.init()
''' size of the screen '''
display_width = 1300
display_height = 700
screen=(display_width,display_height)

black = (2,2,2)   
red = (255,100,0)           
white = (255,255,255)
green = (0,255,0)
green1 = (0,150,0)
blue = (90,100,255)
yellow=(255,255,0)
gree = (3,40,80)
BROWN = (222,184,135)
car_width = 450         
pause=False
gameDisplay = pygame.display.set_mode((screen))
pygame.display.set_caption('Crashing car')
clock = pygame.time.Clock()

obstacleImg = pygame.image.load('mercedes2.png')
carImg = pygame.image.load('ferrari2.png')
treeImg = pygame.image.load('tree1.png')
tree1Img = pygame.image.load('tree2.png')
homeImg = pygame.image.load ('house1.png')
skyImg = pygame.image.load('skyImg.png')
home1Img = pygame.image.load('house2.png')
stoneImg = pygame.image.load('stone.png')
smltreeImg = pygame.image.load('smltree.png')
hillImg = pygame.image.load('hill.png')
crash_sound= pygame.mixer.Sound("crash_sound.wav")



''' display Img'''
def sky(xsky,ysky):
    gameDisplay.blit(skyImg, [xsky,ysky])
def car(x,y):
    gameDisplay.blit(carImg, [x,y])    
def tree(xtree,ytree):
    gameDisplay.blit(treeImg, [xtree,ytree])
def tree1(xtree1,ytree1):
    gameDisplay.blit(tree1Img, [xtree1,ytree1])
def home(xh,yh):
    gameDisplay.blit(homeImg, [xh,yh])   
def home1(xh1,yh1):
    gameDisplay.blit(home1Img, [xh1,yh1])
def stone(sx,sy):
    gameDisplay.blit(stoneImg, [sx,sy])
def smltree(stx,sty):
    gameDisplay.blit(smltreeImg, [stx,sty])
def hill(hx,hy):
    gameDisplay.blit(hillImg, [hx,hy])
def paused():
    pygame.mixer.music.pause()
def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    

def obstacles(obs1_x,obs1_y):
    gameDisplay.blit(obstacleImg, [obs1_x,obs1_y])

def detectCollision(mx1,my1,w1,h1,mx2,my2,w2,h2):
     if (mx2+w2>=mx1>=mx2 and my2+h2>=my1>=my2):
         return True
     elif (mx2+w2>=mx1+w1>=mx2 and my2+h2>=my1>=my2):
         return True
     elif (mx2+w2>=mx1>=mx2 and my2+h2>=my1>=my2):
         return True
     elif (mx2+w2>=mx1+w1>=mx2 and my2+h2>=my1>=my2):
         return True
     else:
         return False
                           
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/6))
    gameDisplay.blit(TextSurf, TextRect)


    pygame.display.update()

    time.sleep(1.5)

    gameLoop()


def database(count):
    conn = sqlite3.connect('Form1.db')

    with conn:

      cursor=conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS highscore (score TEXT)')

    cursor.execute('INSERT INTO highscore (score) VALUES(?)',(count,))
    

    conn.commit ()
    
def Hscores():
    conn = sqlite3.connect('Form1.db')

    with conn:

      cursor=conn.cursor()

    cursor.execute('SELECT MAX(score) from highscore')
    result=cursor.fetchall()
    a= result
    font = pygame.font.SysFont(None, 75)
    text = font.render("High score: "+str(result), True, yellow)
    gameDisplay.blit(text,(display_width//3,display_height//4))
    time.sleep(5)
    conn.commit ()
    
def scores(count):
    font = pygame.font.SysFont(None, 65)
    text = font.render("score: "+str(count), True, red)
    gameDisplay.blit(text,(60,40))

def strip():
    for i in range(0,10):
        pygame.draw.polygon(gameDisplay,white,[(650,200),(650,200),(640,700),(600,700)])
        time.sleep(0.0001)

    
def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display('You Crashed')



def gameLoop():
    global pause
    pygame.mixer.music.load('game_sound.mp3')
    pygame.mixer.music.play(-1)
    x = (display_width * 0.36)          
    y = (display_height * 0.71) 
    xt1,yt1 = 259,324
    
    x_change = 0    
    gameExit=False
    
    xtree1, ytree1= 900,200
    xtree2, ytree2= 350,200
    xh1,yh1 = 700,100
    xh,yh = 330,100
    xtree, ytree= 100,100
    xtreeA, ytreeA= 5,250
    xtreeB, ytreeB= 950,200   #rst
    xtreeC, ytreeC= 1000,50
    sx,sy = 800,250
    sx1,sy1 = 250,400
    stx,sty = 700,150
    stx1,sty1 = 300,150
    stx2,sty2 = 1040,150
    stx3,sty3 = 50,150
    hx,hy = 0,100
    hx1,hy1 = 430,100
    hx2,hy2 = 850,100

    car_height = carImg.get_height()#292
    car_width = carImg.get_width() #458
    obs1_height = obstacleImg.get_height()#135#110 
    obs1_width = obstacleImg.get_width()#190#150
    

    obs1_x = 570
    obs1_y = 150
    obstaclespeed = 1.5
    count=0
    score = 0
    highscore =0
    collision=False
    
    
    while gameExit==False:
      
         home1(xh1,yh1)
         xh1 += 5
         yh1 += 5
         home(xh,yh)
         xh -= 5
         yh += 5
         tree1(xtree2,ytree2) #left tree&stones
         xtree2 -= 5
         ytree2 += 5
         tree1(xtree1,ytree1) #left tree&stones
         xtree1 += 5
         ytree1 += 5
         tree(xtree,ytree)
         xtree -=5
         ytree +=5
         tree(xtreeA,ytreeA)
         xtreeA -=5
         ytreeA +=5
         tree(xtreeB,ytreeB)
         xtreeB +=5
         ytreeB +=5
         tree(xtreeC,ytreeC)
         xtreeC +=5
         ytreeC +=5
         stone(sx,sy)
         sx +=5
         sy +=5
         stone(sx1,sy1)
         sx1 -=5
         sy1 +=5   

         
         
         smltree(stx,sty)
         smltree(stx1,sty1)
         smltree(stx2,sty2)
         smltree(stx3,sty3)
                     
         if count%2==0:
             obstacles(obs1_x,obs1_y)
             obs1_x -= 5
             obs1_y += 5

         else:
             obstacles(obs1_x,obs1_y)
             obs1_x += 5
             obs1_y += 5
         
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True              

            if event.type == pygame.KEYDOWN:     
                if event.key == pygame.K_LEFT:          
                   x_change = -10
                   
                if event.key == pygame.K_RIGHT:       
                    x_change = 10
                      
            if event.type == pygame.KEYUP:             
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   x_change = 0

                   
           
         x += x_change
        
        
         gameDisplay.fill(white)

         pygame.draw.polygon(gameDisplay,blue,[(0,0),(1300,0),(1300,200),(0,200),(0,0)])  #sky
         pygame.draw.polygon(gameDisplay,green1,[(0,200),(650,200),(200,700),(0,700)])          
         pygame.draw.polygon(gameDisplay,gree,[(650,200),(1100,700),(200,700)])  #road
         pygame.draw.polygon(gameDisplay,green1,[(650,200),(display_width,200),(display_width,display_height),(1100,700)]) 
      

              
               
        #sky
         sky(0,0)
         hill(hx,hy)
         hill(hx1,hy1)
         hill(hx2,hy2)
         strip()
         smltree(stx,sty)
         smltree(stx1,sty1)
         smltree(stx2,sty2)
         smltree(stx3,sty3)
         home(xh,yh)  
         home1(xh1,yh1)
         car(x,y)
        #left trees
         tree(xtree,ytree)  
         tree(xtreeA,ytreeA)  
         tree(xtreeC,ytreeC)  
         tree1(xtree1,ytree1) 
         tree(xtreeB,ytreeB)  
        
         tree1(xtree2,ytree2) 
         
         
        
         stone(sx,sy) 
         stone(sx1,sy1)
        
       
         obstacles(obs1_x,obs1_y)
         obs1_y += obstaclespeed
         
         car(x,y)
         
        
         
         if x > display_width - 560 or x < 190:
            crash()
            gameExit = True

         else:
          if obs1_y > display_height:
            obs1_y = 150
            obs1_x = 550
            count += 1
        
            obstaclespeed += 1
         if y < obs1_y + obs1_height:
             print('y crossover')
             if x > obs1_x and x < obs1_x + obs1_width or x + car_width > obs1_x and x + car_width < obs1_x + obs1_width:
                 print('x crossover')
                 crash()
                 database(count)
                 Hscores()
                 time.sleep(0.5)
                 #yourscore(count)
                 gameExit = True

         
         scores(count)

         pygame.display.flip()
         pygame.display.update()
         clock.tick(120)

         
         
   
gameLoop()

pygame.quit()
quit()
