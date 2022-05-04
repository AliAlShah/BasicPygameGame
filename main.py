import pygame 
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

FPS = 60


GREYBLUESPACESHIPIMAGE = pygame.image.load(
    os.path.join('Assets', 'bluegreyspaceship.png'))
GREYBLUESPACESHIP =  pygame.transform.scale(GREYBLUESPACESHIPIMAGE, (40, 40))

GREYREDSPACESHIPIMAGE = pygame.image.load(
    os.path.join("Assets", "redgreyspaceship.png"))
GREYREDSPACESHIP = pygame.transform.rotate(pygame.transform.scale(GREYREDSPACESHIPIMAGE, (40, 30)), 270)


def draw_window():
    WIN.fill((255, 255, 255))
    WIN.blit(GREYBLUESPACESHIP, (300, 100))
    WIN.blit(GREYREDSPACESHIP, (600, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()