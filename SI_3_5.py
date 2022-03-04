
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

background_image = pygame.image.load("bg.jpg").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()
player_image = pygame.image.load("player.png").convert_alpha()

#creating objects of game
player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

enemies=[]

for j in range(1,5): 
    for i in range(1,5):
        enemies.append( pygame.Rect(i*70,j*50,40,40) )

bullet=pygame.Rect(200,400,5,10)
bulletspeed=50
bulletState="ready"
        
while True:    
    screen.fill((0,0,0))
    screen.blit(background_image,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            if event.key ==pygame.K_RIGHT:
                player.x +=playerSpeed
            if event.key == pygame.K_SPACE:
                bulletState="fired"
    
    if bulletState == "ready":
        bullet.x=player.x+17
        bullet.y=player.y+12
    
    if bulletState =="fired":
       bullet.y=bullet.y-bulletspeed
       if bullet.y<0:
           bulletState="ready"
    
    
    for enemy in enemies:
        enemy.x= enemy.x + enemyspeed
        
        if enemy.x == 0 or enemy.x==380:
            enemyspeed=enemyspeed * -1
            for e in enemies:
                e.y=e.y+20
        
        if bullet.colliderect(enemy):
            enemy.y=-9000
            bullet.y=-9000
        
        #2 Check if enemy is collided with the player and then move the player outside the game screen.
        if player.colliderect(enemy):
                player.y=9000
                
        #1 Add code and replace this line to show enemy image instead of a rectangle.
       # pygame.draw.rect(screen,(123,200,100),enemy)
        screen.blit(enemy_image,enemy)
        
    pygame.draw.rect(screen,(225,225,15),bullet)         
    #pygame.draw.rect(screen,(23,100,100),player)
    screen.blit(player_image,player)
       
    
    pygame.display.update()
    clock.tick(30)
