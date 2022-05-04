import pygame 
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

FPS = 60
SPEED= 5
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

GREYBLUESPACESHIPIMAGE = pygame.image.load(
    os.path.join('Assets', 'bluegreyspaceship.png'))
GREYBLUESPACESHIP =  pygame.transform.scale(GREYBLUESPACESHIPIMAGE, (40, 40))

GREYREDSPACESHIPIMAGE = pygame.image.load(
    os.path.join("Assets", "redgreyspaceship.png"))
GREYREDSPACESHIP = pygame.transform.rotate(pygame.transform.scale(GREYREDSPACESHIPIMAGE, (40, 30)), 270)


def draw_window(blue, red):
    WIN.fill((255, 255, 255))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    WIN.blit(GREYBLUESPACESHIP, (blue.x, blue.y))
    WIN.blit(GREYREDSPACESHIP, (red.x,  red.y))
    pygame.display.update()

def blue_handle_movement(keys_pressed, blue):
    if keys_pressed[pygame.K_a] and blue.x - SPEED > 0: #Left
        blue.x -= SPEED

    if keys_pressed[pygame.K_d] and blue.x + SPEED + blue.width < BORDER.x: #Right
        blue.x += SPEED

    if keys_pressed[pygame.K_w] and blue.y - SPEED > 0: #Up
        blue.y -= SPEED

    if keys_pressed[pygame.K_s]and blue.y + SPEED + blue.height < HEIGHT: #Down
        blue.y += SPEED

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - SPEED > BORDER.x + BORDER.width: #Left
        red.x -= SPEED

    if keys_pressed[pygame.K_RIGHT] and red.x + SPEED + red.width < WIDTH + 7: #Right
        red.x += SPEED

    if keys_pressed[pygame.K_UP] and red.y - SPEED > 0: #Up
        red.y -= SPEED

    if keys_pressed[pygame.K_DOWN] and red.y + SPEED + red.height < HEIGHT + - 10: #Down
        red.y += SPEED

def main():
    blue = pygame.Rect(100, 300, 40, 40)
    red = pygame.Rect(700, 300, 40, 30)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        blue_handle_movement(keys_pressed, blue)
        red_handle_movement(keys_pressed, red)

        draw_window(blue, red)

    pygame.quit()

if __name__ == "__main__":
    main()