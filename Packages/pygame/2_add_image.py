import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Window")

# To load the image
image = pygame.image.load("E:\\bike.jpg")

while True:
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()