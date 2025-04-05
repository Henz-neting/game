import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

# Font
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def show_message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH // 6, HEIGHT // 3])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    # Random food
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            show_message("Game Over! Press R to Restart or Q to Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

        x += x_change
        y += y_change

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        # Check self collision
        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        draw_snake(snake)
        pygame.display.update()

        # Check food collision
        if x == food_x and y == food_y:
            snake_length += 1
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

        clock.tick(FPS)

    pygame.quit()

game_loop()
import pygame

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame!")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Exit pygame
pygame.quit()
