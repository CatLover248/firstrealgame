import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Example")



class Square:
    def __init__(self, size, gravity, x, y):
        self.size = size
        self.gravity = gravity
        self.x = x
        self.y = y
    
    def collision(self,enemy):
        # I do not really understand how this works :( 
        if self.x < enemy.x + enemy.size and self.x + self.size > enemy.x and self.y < enemy.y + enemy.size and self.y + self.size > enemy.y:
            return True
        return False

class Enemy:
    def __init__(self, size, gravity, x, y):
        self.size = size
        self.gravity = gravity
        self.x = x
        self.y = y


# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,0,0)
LIGHT_GREEN = (94, 191, 120)

square = Square(50, 0, (screen_width/2)-50,(screen_height/2)-50)
enemies = []

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 30)

for i in range(5):
    e = Enemy(50, -5, random.randrange(0,screen_width), random.randrange(0,screen_height))
    enemies.append(e)

def physics_process():
    #square.y -= square.gravity
    for e in enemies:
        e.y -= e.gravity
        if e.y > screen_height or e.x > screen_width:
            e.y = -50
            e.x = random.randrange(0, screen_width)
        if square.collision(e):
            square.x = (screen_width/2)-50
            square.y = (screen_height/2)-50
            for e in enemies:
                enemies.remove(e)
            
            for i in range(5):
                e = Enemy(50, -5, random.randrange(0,screen_width), random.randrange(0,screen_height))
                enemies.append(e)

            start()

def draw():
    pygame.draw.rect(screen, LIGHT_GREEN, (0,0,screen_width, screen_height))
    pygame.draw.rect(screen, BLUE, (square.x, square.y, square.size, square.size))

    for e in enemies:
        pygame.draw.rect(screen, RED, (e.x, e.y, e.size, e.size))

def start():
    start_running = True
    while start_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Fill the screen with white
        screen.fill(LIGHT_GREEN)

        text_surface = font.render("Don't collide with the red squares. -Yusuf", True, WHITE)
        text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
        text_surface_small = small_font.render("Press Space to Play!", True, WHITE)
        text_rect_small = text_surface_small.get_rect(center=(screen_width/2, (screen_height/2)+50))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface_small, text_rect_small)
        # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()
        
        # Move the square based on arrow key presses
        if keys[pygame.K_SPACE]:
            game()


        clock.tick(FPS)


        # Update the display
        pygame.display.flip()
def game():


    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Fill the screen with white
        screen.fill(WHITE)

        # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()
        
        # Move the square based on arrow key presses
        if keys[pygame.K_LEFT]:
            square.x -= 5
        if keys[pygame.K_RIGHT]:
            square.x += 5
        if keys[pygame.K_UP]:
            square.y -= 5
        if keys[pygame.K_DOWN]:
            square.y += 5


        physics_process()

        # Draw the square
        draw()


        clock.tick(FPS)


        # Update the display
        pygame.display.flip()

start()

# Quit Pygame
pygame.quit()
sys.exit()
