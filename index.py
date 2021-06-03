import sys
import pygame
import math
from pygame.locals import QUIT
from pygame.locals import Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("pygame window")
FPSCLOCK = pygame.time.Clock()

class Block:
    def __init__(self,color,rect):
        self.color = block_color
        self.rect = block_rect

    def draw(self):
        pygame.draw.rect(SURFACE,self.color,self.rect)
        
class Ball:
    def __init__(self,color,rect,dir,speed):
        self.color = ball_color
        self.rect = ball_rect
        self.dir = ball_dir
        self.speed = ball_speed

    def draw(self):
        pygame.draw.ellipse(SURFACE,self.color,self.rect)
        
    def move(self):
            if self.rect.centerx < 0 or self.rect.centerx > 400:
                self.dir = 180-self.dir
            if self.rect.centery < 0 or self.rect.centery > 300:
                self.dir = -self.dir

            self.rect.centerx += math.cos(math.radians(self.dir))*self.speed
            self.rect.centery -= math.sin(math.radians(self.dir))*self.speed
        
#Block
left = 50
top = 50
width = 45
height = 20
block_color = (200,50,200)
block_rect = Rect(left,top,width,height)
block = Block(block_color,block_rect)

blocks = []

for i in range(6):
    top = 50
    
    for j in range(4):
        top=top+25
        block_rect = Rect(left,top,width,height)
        blocks.append(Block(block_color,block_rect))
    left=left+50
        
#Ball
ball_rect = Rect(150,100,10,10)
ball_color = (255,255,0)
ball_dir = 10
ball_speed = 20
ball = Ball(ball_color,ball_rect,ball_speed,ball_dir)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SURFACE.fill((0,0,0))
    for block in blocks:
        block.draw()
    ball.draw()
    ball.move()

    tmp_blocks = []

    for block in blocks:
        if ball.rect.colliderect(block.rect) != True:
            tmp_blocks.append(block)
    blocks = tmp_blocks

    pygame.display.update()
    FPSCLOCK.tick(30)
