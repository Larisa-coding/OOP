import pygame
import random
import sys

WIDTH, HEIGHT = 550, 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гонки")
clock = pygame.time.Clock()

road_image = pygame.image.load('road.png').convert()
car_image = pygame.image.load('car.png').convert_alpha()
obstacle_image = pygame.image.load('obstacle.png').convert_alpha()

car_image = pygame.transform.scale(car_image, (50, 100))
obstacle_image = pygame.transform.scale(obstacle_image, (50, 100))

class Player:
    def __init__(self):
        self.rect = car_image.get_rect(center=(WIDTH // 2, HEIGHT - 150))

    def move(self, dx):
        if 0 < self.rect.x + dx < WIDTH - 50:
            self.rect.x += dx

    def draw(self):
        screen.blit(car_image, self.rect)

class Obstacle:
    def __init__(self):
        self.rect = obstacle_image.get_rect(center=(random.randint(60, WIDTH - 60 - 50), random.randint(-150, -100)))

    def move(self):
        self.rect.y += 9

    def draw(self):
        screen.blit(obstacle_image, self.rect)

def check_collision(obstacles, player):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            return True
    return False

def game_loop():
    player = Player()
    obstacles = []
    score = 0
    max_obstacles = 5
    game_over = False

    background_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-7)
        if keys[pygame.K_RIGHT]:
            player.move(7)

        if len(obstacles) < max_obstacles:
            if random.randint(1, 30) == 1:
                obstacles.append(Obstacle())

        for obstacle in obstacles[:]:
            obstacle.move()
            if obstacle.rect.top > HEIGHT:
                obstacles.remove(obstacle)

        background_y += 7
        if background_y >= HEIGHT:
            background_y = 0

        screen.blit(road_image, (0, background_y - HEIGHT))
        screen.blit(road_image, (0, background_y))

        player.draw()
        for obstacle in obstacles:
            obstacle.draw()

        if game_over:
            font = pygame.font.SysFont(None, 40)
            text = font.render("Смотри куда едешь!", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
            text = font.render("Начать новую игру? Да (Y) / Нет (N)", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - 250, HEIGHT // 2 + 20))

            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            waiting = False
                            game_loop()
                        if event.key == pygame.K_n:
                            pygame.quit()
                            sys.exit()
        else:
            if check_collision(obstacles, player):
                game_over = True

            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
