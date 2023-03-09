import pygame
import sys

pygame.init()
size = width, height = 1800, 800  # 窗口大小
screen = pygame.display.set_mode(size)
color = (232, 232, 232)
ball = pygame.image.load('apple.png')  # 图片导入
action = ball.get_rect()
zhou = [1, 1]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    action = action.move(zhou)
    if action.left < 0 or action.right > width:
        zhou[0] = -zhou[0]
    if action.top < 0 or action.bottom > height:
        zhou[1] = -zhou[1]

    screen.fill(color)
    screen.blit(ball, action)
    pygame.display.flip()


