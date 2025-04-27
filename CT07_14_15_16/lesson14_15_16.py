import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_caption("Pong Game")

y1 = 300
paddleHeight = 50

running = True
while running:
    pygame.draw.rect(screen, green, )



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()