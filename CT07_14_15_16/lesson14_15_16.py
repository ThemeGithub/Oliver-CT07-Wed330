import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

speed = 1.8
y1 = height // 2
y2 = height // 2
paddleHeight = 100
paddleWidth = 20

ballsize = 20
ballx = width // 2
bally = height // 2
dx = 2
dy = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y1 -= speed
    if keys[pygame.K_s]:
        y1 += speed

    if keys[pygame.K_UP]:
        y2 -= speed
    if keys[pygame.K_DOWN]:
        y2 += speed

    if y1 < 0:
        y1 = 0
    if y1 > height - paddleHeight:
        y1 = height - paddleHeight



    screen.fill((0, 0, 0))

    paddle1 = pygame.draw.rect(screen, (0, 100, 0), (10, y1 - paddleHeight / 2, paddleWidth, paddleHeight))
    paddle2 = pygame.draw.rect(screen, (100, 0, 0), (width - paddleWidth - 10, y2 - paddleHeight / 2, paddleWidth, paddleHeight))
    pygame.draw.circle(screen, (0, 255, 255), (ballx, bally), ballsize)

    ballx += dx
    bally += dy
    
    if bally < 0 or bally > width:
        dy = dy * -1
    
    if ballx < paddle1.right + ballsize and bally > paddle1.top and bally < paddle1.bottom:
        dx = dx * -1
    if ballx < paddle2.left + ballsize and bally > paddle2.top and bally < paddle2.bottom:
        dx = dx * -1

    pygame.display.flip()
pygame.quit()