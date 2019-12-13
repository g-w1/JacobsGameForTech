#module setup
import pygame, os, sys
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
pygame.mixer.pre_init(44100,16,2,4096)    
pygame.init()
pygame.font.init()
#variable setup        
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Save Me', False, (0, 0, 0))
frame_rate=30
colli = False
tiles = []
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Nature Platformer")
leaf = (144,204,7)
grass = (149,218,80)
dirt = (101,86,81)
bark = (167,158,143)
lava = (247,176,66)
sun = (243,194,13)
platform = (1,136,85)
run_start = True
run_inst = True
run_lvl_1 = True
run_lvl_2 = True
run_lvl_3 = True
run_lvl_4 = True
gameover = True
run_cutscene = True
lvl_1 = [[(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,leaf,leaf],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),platform,(0,),(0,),platform,(0,),bark,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [grass, grass,grass,grass,(0,),(0,),grass,grass,grass,grass],
         [dirt,dirt,dirt,dirt,(0,),(0,),dirt,dirt,dirt,dirt],
         [dirt,dirt,dirt,dirt,lava,lava,dirt,dirt,dirt,dirt]]
lvl_2 = [[(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),sun],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,)],
        [(0,),(0,),(0,),(0,),platform,(0,),(0,),leaf,(0,),leaf],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),platform,(0,),(0,),platform,(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [grass, grass,grass,(0,),(0,),(0,),(0,),(0,),grass,grass],
         [dirt,dirt,dirt,(0,),(0,),(0,),(0,),(0,),dirt,dirt],
         [dirt,dirt,dirt,lava,lava,lava,lava,lava,dirt,dirt]]
lvl_3 = [[(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),sun],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,leaf,leaf],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [grass, grass,grass,(0,),(0,),(0,),(0,),(0,),grass,grass],
         [dirt,dirt,dirt,(0,),(0,),(0,),(0,),(0,),dirt,dirt],
         [dirt,dirt,dirt,lava,lava,lava,lava,lava,dirt,dirt]]
lvl_4 = [[(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),sun],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),leaf,leaf,leaf],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
        [(0,),(0,),(0,),(0,),(0,),(0,),(0,),(0,),bark,(0,)],
         [grass, grass,grass,(0,),(0,),(0,),(0,),(0,),grass,grass],
         [dirt,dirt,dirt,(0,),(0,),(0,),(0,),(0,),dirt,dirt],
         [dirt,dirt,dirt,lava,lava,lava,lava,lava,dirt,dirt]]
monkey = pygame.image.load("monkey3.png").convert_alpha()
bear1 = pygame.image.load("beargd2.png").convert_alpha()
start_screen = pygame.image.load("startscreen.png").convert()
instructions = pygame.image.load("instructions.png").convert()
cutscene = pygame.image.load("cutscene2.png").convert()
heart = pygame.image.load("heart3.png").convert_alpha()
gameover1 = pygame.image.load("gameover.png").convert()
rhino1 = pygame.image.load("rhino3.png").convert_alpha()
ant1 = pygame.image.load("ant3.png").convert_alpha()
lion1 = pygame.image.load("lion3.png").convert_alpha()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)

#class setup
class player(object):
    def __init__(self,x,y,image):
        self.grav = 0
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.vel = 8
        self.isJump = False
        self.jumpCount = 8
        self.jumpCountG = 8
        self.velo = -10
        self.health = 3
        self.rect = pygame.Rect(x,y,image.get_width(),image.get_height())
        self.colli = True
    def collision_1(self):
        global tiles
        for tile in tiles:
            if self.rect.colliderect(pygame.Rect(tile.x,tile.y-5,50,25)):
                    return True
            else:return False
    def collison(self):
        self.rec = pygame.Rect(self.x,self.y,self.width,self.height)
        for tile in tiles:
            if self.rec.colliderect(pygame.Rect(tile.x,tile.y-1,50,51)):
                self.y=tile.y-self.height
                self.isJump=False
                self.grav = 0
                self.colli = False
            else:
                self.colli = True
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                pass
    def win(self,level):
        self.rec = pygame.Rect((self.x,self.y,self.width,self.height))
        if self.rec.colliderect(pygame.Rect(400,5,76,100)):
            level=False
    def gravity(self, accel):
        if colli == False and self.isJump == False:
            self.y -= self.velo
            '''if self.velo<=25:
                self.velo -= accel'''
    def did_die(self):
        if self.y>=405:
            self.x=2
            self.y=330
            self.isJump= False
            self.velo=-10
            self.health-=1
        if self.health == 3:
            win.blit(heart,(0,0))
            win.blit(heart,(50,0))
            win.blit(heart,(100,0))
        if self.health == 2:
            win.blit(heart,(0,0))
            win.blit(heart,(50,0))
        if self.health == 1:
            win.blit(heart,(0,0))
        if self.health==0:
            global run_start
            global run_inst
            global run_lvl_1
            global run_lvl_2
            global run_lvl_3
            global run_lvl_4
            global run_cutscene
            global gameover
            global run_cutscene
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = True
            run_cutscene = False
class Tile(object):
    def __init__(self, xpos, ypos, rgb):
        self.x=xpos
        self.y=ypos
        self.width = 50
        self.height=50
        self.rgb=rgb
        self.rect = pygame.Rect(xpos, ypos, 50,50)
#start screen
while run_start:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False
            break
    pressed_keys = pygame.key.get_pressed()
    win.fill((0,20,20))
    win.blit(start_screen,(0,0))
    if pygame.mouse.get_pressed()[0] and pygame.Rect((96,160,300,150)).collidepoint(pygame.mouse.get_pos()):
        run_start = False
    pygame.display.update()
#instructions screen
while run_inst:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False
            break
    pressed_keys = pygame.key.get_pressed()
    win.fill((0,20,20))
    win.blit(instructions,(0,0))
    if pressed_keys[pygame.K_SPACE]:
        run_inst = False
    pygame.display.update()
#cutscene
pygame.mixer.music.play(-1)
while run_cutscene:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False
    pressed_key = pygame.key.get_pressed()
    win.blit(cutscene,(0,0))
    if pressed_key[pygame.K_SPACE]:
        run_cutscene= False
    pygame.display.update()
#level function
def level(player, lvl_,run_lvl, image_of_player,person_to_be_saved):
    global run_start
    global run_inst
    global run_lvl_1
    global run_lvl_2
    global run_lvl_3
    global run_lvl_4
    global run_cutscene
    global gameover
    global run_cutscene
    global frame_rate
    global bear1
    global monkey
    tiles = []
    for ypos in range(0,10):
        for xpos in range(0,10):
            if lvl_1[ypos][xpos]!= (0,):
                tiles.append(Tile(50*xpos,50*ypos,lvl_[ypos][xpos]))  

    while run_lvl:
        player.rec = pygame.Rect((player.x,player.y,player.width,player.height))
        if player.rec.colliderect(pygame.Rect(400,5,76,100)):
                run_lvl_1=False
        pygame.time.delay(frame_rate)
        player.did_die()
        player.gravity(.1)
        player.collison()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_start = False
                run_inst = False
                run_lvl_1 = False
                run_lvl_2 = False
                run_lvl_3 = False
                run_lvl_4 = False
                run_cutscene = False
                gameover = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > player.vel: 
            player.x -= player.vel
        if keys[pygame.K_RIGHT] and player.x < 500 - player.vel - player.width:  
            player.x += player.vel
        if player.isJump==False: 
            if (keys[pygame.K_UP] | keys[pygame.K_SPACE]) and player.collision_1():
                player.isJump = True
                player.y-=1
        else:
            if player.jumpCount >= player.collision_1():
                player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
                player.jumpCount -= 1
            else: 
                player.jumpCount = 8
                player.jumpCountG = player.jumpCount
                player.isJump = False
        
        win.fill((50,0,200))
        for tile in tiles:
            pygame.draw.rect(win, tile.rgb, (tile.x, tile.y, tile.width, tile.height))
        win.blit(image_of_player,(player.x,player.y))
        player.did_die()
        win.blit(person_to_be_saved,(400,5))
        win.blit(textsurface,(300,0))
        pygame.display.update()
level(player(5,330,bear1),lvl_1,run_lvl_1,bear1,monkey)
    #game loop for level 1 end
    #stuff for level 2
'''rhino = player(2,330,rhino1)
    tiles = []
    for ypos in range(0,10):
        for xpos in range(0,10):
            if lvl_2[ypos][xpos]!= (0,):
                tiles.append(Tile(50*xpos,50*ypos,lvl_2[ypos][xpos]))
#game loop for level 2 start
while run_lvl_2:
    print(rhino.y)
    rhino.rec = pygame.Rect((rhino.x,rhino.y,rhino.width,rhino.height))
    if rhino.rec.colliderect(pygame.Rect(400,5,76,100)):
        run_lvl_2=False
    pygame.time.delay(frame_rate)
    rhino.did_die()
    rhino.gravity(.1)
    rhino.collison()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and rhino.x > rhino.vel: 
        rhino.x -= rhino.vel

    if keys[pygame.K_RIGHT] and rhino.x < 500 - rhino.vel - rhino.width:  
        rhino.x += rhino.vel
        
    if rhino.isJump==False: 
      
        if (keys[pygame.K_UP] | keys[pygame.K_SPACE]) and (rhino.isJump == False and rhino.colli == True):
            rhino.isJump = True
            rhino.y-=1
    else:
        if rhino.jumpCount >= -1*rhino.jumpCountG:
            rhino.y -= (rhino.jumpCount * abs(rhino.jumpCount)) * 0.5
            rhino.jumpCount -= 1
        else: 
            rhino.jumpCount = 8
            rhino.jumpCountG = rhino.jumpCount
            rhino.isJump = False
    
    win.fill((100,0,200))
    for tile in tiles:
        pygame.draw.rect(win, tile.rgb, (tile.x, tile.y, tile.width, tile.height))
    win.blit(rhino1,(rhino.x,rhino.y))
    rhino.did_die()
    win.blit(lion1,(400,55))
    win.blit(textsurface,(300,0))
    pygame.display.update()
#game loop for level 2 end
#stuff for level 3
lion = player(2,330,lion1)
tiles = []
for ypos in range(0,10):
    for xpos in range(0,10):
        if lvl_3[ypos][xpos]!= (0,):
            tiles.append(Tile(50*xpos,50*ypos,lvl_3[ypos][xpos]))
#game loop for level 3 start
while run_lvl_3:
    lion.rec = pygame.Rect((lion.x,lion.y,lion.width,lion.height))
    if lion.rec.colliderect(pygame.Rect(400,5,76,100)):
           run_lvl_3 = False
           gameover = False

    pygame.time.delay(frame_rate)
    lion.did_die()
    lion.gravity(.1)
    lion.collison()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and lion.x > lion.vel: 
        lion.x -= rhino.vel

    if keys[pygame.K_RIGHT] and lion.x < 500 - lion.vel - lion.width:  
        lion.x += lion.vel
        
    if lion.isJump==False: 
      
        if (keys[pygame.K_UP] | keys[pygame.K_SPACE]) and (lion.isJump == False and lion.collision_1):
            lion.isJump = True
            lion.y-=1
    else:
        if lion.jumpCount >= -1*lion.jumpCountG:
            lion.y -= (lion.jumpCount * abs(lion.jumpCount)) * 0.5
            lion.jumpCount -= 1
        else: 
            lion.jumpCount = 8
            lion.jumpCountG = lion.jumpCount
            lion.isJump = False
    
    win.fill((100,0,200))
    for tile in tiles:
        pygame.draw.rect(win, tile.rgb, (tile.x, tile.y, tile.width, tile.height))
    win.blit(lion1,(lion.x,lion.y))
    lion.did_die()
    win.blit(ant1,(400,5))
    win.blit(textsurface,(300,0))
    pygame.display.update()
#game loop for level 3 end'''
while gameover == True:
    win.blit(gameover1, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_start = False
            run_inst = False
            run_lvl_1 = False
            run_lvl_2 = False
            run_lvl_3 = False
            run_lvl_4 = False
            run_cutscene = False
            gameover = False
pygame.quit()
