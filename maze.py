from pygame import *
 
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <420:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 630:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,c1,c2,c3,x,y,w,h):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('g.jpg'),(700,500))

game = True
finish = False
clock = time.Clock()
FPS = 120
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg') 

player = Player('ghj.jpg',5,435,1)
monster = Enemy('amogys.png',600,250,2)
gold = GameSprite('treasure.png',600,400,0)

w1 = Wall(45,255,228,100,20,450,10)
w2 = Wall(45,255,228,100,120,10,350)
w3 = Wall(45,255,228,100,120,50,10)
w4 = Wall(45,255,228,220,20,10,300)
w5 = Wall(45,255,228,160,410,100,10)
w6 = Wall(45,255,228,310,200,10,350)
w7 = Wall(45,255,228,400,90,10,300)
w8 = Wall(45,255,228,570,340,10,150)

font.init()
font = font.Font(None,70)
lose = font.render('Loser',True,(255,30,0))
win = font.render('Win!',True,(0,255,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        player.update()    
        monster.reset()
        monster.update()
        gold.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
    
        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or    sprite.collide_rect(player,w3) or \
            sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or \
            sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8):
            finish = True
            window.blit(lose,(400,200))
            kick.play()
        if sprite.collide_rect(player,gold):
            finish = True
            window.blit(win,(400,200))
            money.play()
    
    
    
    
    display.update()
    clock.tick(FPS)