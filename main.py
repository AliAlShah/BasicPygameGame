import pygame 
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

FPS = 60
SPEED= 5
BULLET_SPEED = 7
MAX_BULLETS = 3

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(
    os.path.join("Assets", "laserhit.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join("Assets", "lasershoot.mp3"))

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "background.png")), (WIDTH, HEIGHT))

GREYBLUESPACESHIPIMAGE = pygame.image.load(
    os.path.join('Assets', 'bluegreyspaceship.png'))
GREYBLUESPACESHIP =  pygame.transform.scale(GREYBLUESPACESHIPIMAGE, (40, 40))

GREYREDSPACESHIPIMAGE = pygame.image.load(
    os.path.join("Assets", "redgreyspaceship.png"))
GREYREDSPACESHIP = pygame.transform.rotate(pygame.transform.scale(GREYREDSPACESHIPIMAGE, (40, 30)), 270)


def draw_window(blue, red, red_bullets, blue_bullets, red_health, blue_health):
    WIN.blit(BACKGROUND, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, (255, 255, 255))
    blue_health_text = HEALTH_FONT.render("Health: " + str(blue_health), 1, (255, 255, 255))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(blue_health_text, (10, 10))

    WIN.blit(GREYBLUESPACESHIP, (blue.x, blue.y))
    WIN.blit(GREYREDSPACESHIP, (red.x,  red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    for bullet in blue_bullets:
        pygame.draw.rect(WIN, (0, 0, 255), bullet)
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

def handle_bullets(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.x += BULLET_SPEED
        
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    blue = pygame.Rect(100, 300, 40, 40)
    red = pygame.Rect(700, 300, 40, 30)
    blue_bullets = []
    red_bullets = []
    red_health = 10
    blue_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        blue.x + blue.width, blue.y + blue.height//2 - 2, 10, 5)
                    blue_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == BLUE_HIT:
                blue_health -= 1
                BULLET_HIT_SOUND.play()
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "Blue Wins!"

        if blue_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
        
        
        keys_pressed = pygame.key.get_pressed()
        blue_handle_movement(keys_pressed, blue)
        red_handle_movement(keys_pressed, red)

        handle_bullets(blue_bullets, red_bullets, blue, red)

        draw_window(blue, red, red_bullets, blue_bullets, red_health, blue_health)

    main()

if __name__ == "__main__":
    main()