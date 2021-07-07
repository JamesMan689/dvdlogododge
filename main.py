import pygame
from random import randint
import time
import math

pygame.init()
win = pygame.display.set_mode((800, 600))
color = (255, 255, 255)
pygame.display.set_caption('DVD Logo Dodge')
font = pygame.font.SysFont('Courier', 25)
gameOver = font.render("Game Over", True, (255, 0, 0))

x = 200
y = 200
width = 20
height = 20
speed = .3
logo = pygame.image.load('dvd.png')
logo = pygame.transform.scale(logo, (100, 100))
img_size = logo.get_rect().size
xcor = randint(50, 800 - 60)
ycor = randint(50, 600 - 60)
x_speed = 1
y_speed = 1
n = 0



def move(a, b):
    win.blit(logo, (xcor, ycor))


def collision(x, y, xcor, ycor):
    distance = math.sqrt((math.pow(x - xcor, 2)) + (math.pow(y - ycor, 2)))
    if distance < 40:
        return True
    else:
        return False


running = True
while running:
    win.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 800 - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += speed
    if keys[pygame.K_ESCAPE]:
        break
    if (xcor + img_size[0] >= 800) or (xcor <= 0):
        x_speed = -x_speed
    if (ycor + img_size[1] >= 600) or (ycor <= 0):
        y_speed = -y_speed
    xcor += x_speed
    ycor += y_speed
    move(xcor, ycor)
    rectangle = pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    score = font.render("Score: " + str(n), True, (0, 0, 255))
    win.blit(score, (100, 10))
    n += 1
    if_collision = collision(x, y, xcor, ycor)
    if if_collision:
        win.blit(gameOver, (350, 10))
        pygame.display.flip()
        time.sleep(2)
        break
    pygame.display.update()
pygame.quit()
