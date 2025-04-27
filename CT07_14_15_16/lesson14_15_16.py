import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

y1 = height // 2
y2 = height // 2
y1s = 0
y2s = 0
paddleHeight = 100
paddleWidth = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, (0, 100, 0), (10, y1 - paddleHeight / 2, paddleWidth, paddleHeight))
    pygame.draw.rect(screen, (100, 0, 0), (width - paddleWidth - 10, y2 - paddleHeight / 2, paddleWidth, paddleHeight))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y1s -= 0.5
    if keys[pygame.K_s]:
        y1s += 0.5

    y1 += y1s
    if y1 < 0:
        y1 = 0
        y1s = 0
    if y1 > height - paddleHeight:
        y1 = height - paddleHeight
        y1s = 0

    y1s = y1s * 0.9
    pygame.display.flip()
pygame.quit()