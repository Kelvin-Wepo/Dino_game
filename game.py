import pygame
import random

# Window dimensions
WIDTH = 800
HEIGHT = 300

# Player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = (0, 255, 0)

# Obstacle dimensions
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50
OBSTACLE_COLOR = (255, 0, 0)

# Gravity
GRAVITY = 1

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT - PLAYER_HEIGHT - 10
        self.velocity = 0

    def jump(self):
        self.velocity = -15

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > HEIGHT - PLAYER_HEIGHT - 10:
            self.y = HEIGHT - PLAYER_HEIGHT - 10
            self.velocity = 0

    def draw(self):
        pygame.draw.rect(window, PLAYER_COLOR, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))

class Obstacle:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - OBSTACLE_HEIGHT - 10
        self.width = OBSTACLE_WIDTH

    def update(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(window, OBSTACLE_COLOR, (self.x, self.y, self.width, OBSTACLE_HEIGHT))

player = Player()
obstacles = []

score = 0
font = pygame.font.Font(None, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    window.fill((255, 255, 255))

    if random.randint(0, 100) < 2:
        obstacles.append(Obstacle())

    for obstacle in obstacles:
        obstacle.update()
        obstacle.draw()
        if obstacle.x < -OBSTACLE_WIDTH:
            obstacles.remove(obstacle)

        if obstacle.x == player.x + PLAYER_WIDTH:
            score += 1

        if obstacle.x < player.x + PLAYER_WIDTH and obstacle.x + OBSTACLE_WIDTH > player.x and player.y + PLAYER_HEIGHT > obstacle.y:
            running = False

    player.update()
    player.draw()

    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
