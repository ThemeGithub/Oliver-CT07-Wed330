import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_caption("Pong Game")

y1 = 300
paddleHeight = 100
paddleWidth = 20

running = True
while running:
    pygame.draw.rect(screen, "green", (10, y1 - paddleHeight / 2, paddleWidth, paddleHeight))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()