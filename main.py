import pygame
import os
import time
import random

pygame.font.init()
WIDTH, HEIGHT = 1280, 720
FPS = 60
clock = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HuntyHealth")

# Player ship
PLAYER_BAG = pygame.transform.scale(pygame.image.load(os.path.join('assest', "shoppingBag.png")), (150, 150))
# playerS
playerS_HAMBURGER = pygame.image.load(os.path.join("assest", "burger.png"))
playerS_CARROT = pygame.image.load(os.path.join("assest", "carrot.jpg"))
playerS_CABBAGE = pygame.image.load(os.path.join("assest", "cabage.jpg"))
playerS_salmon = pygame.image.load(os.path.join("assest", "salmon.jpg"))
playerS_TOMATOES = pygame.image.load(os.path.join("assest", "tomato.jpg"))
# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assest", 'bg.jpg')), (WIDTH, HEIGHT))
BG_BOWL = pygame.transform.scale(pygame.image.load(os.path.join("assest", 'bowlmiddle.png')), (150, 150))


class Fruit:
    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.player_drop = None
        self.line = []
        self.counter = 0

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def get_width(self):
        return self.player_img.get_width()

    def get_height(self):
        return self.player_img.get_height()


class Player(Fruit):
    def __init__(self, x, y, health=3):
        super().__init__(x, y, health)
        self.player_img = PLAYER_BAG
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health


class FruitDrop(Fruit):
    FRUIT_MAP = {
        "tomatoes": playerS_TOMATOES,
        "carrot": playerS_CARROT,
        "salmon": playerS_salmon,
        "cabbage": playerS_CABBAGE,
        "hamburger": playerS_HAMBURGER,
    }

    def __init__(self, x, y, types):
        super().__init__(x, y)
        self.player_img = self.FRUIT_MAP[types]
        self.mask = pygame.mask.from_surface(self.player_img)

    def move(self, vel):
        self.y += vel


def main():
    running = True
    user = "Test User"
    point = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 36)
    player = Player(300, 550)
    player_vel = 6

    # Enemy Init

    fruit_drop = []
    wave_length = 5
    fruit_drop_vel = 1

    def draw_window():
        WIN.blit(BG, (0, 0))

        # draw text
        user_label = main_font.render(f"Username: {user}", 1, (255, 80, 100))
        point_label = main_font.render(f"Ingredients point: {point}", 1, (0, 255, 255))
        next_label = main_font.render(f"Next Ingredient : ", None, (255, 255, 255))
        WIN.blit(user_label, (10, 10))
        WIN.blit(point_label, (WIDTH - point_label.get_width() - 10, 10))
        WIN.blit(next_label, (10, 50))

        for fruits in fruit_drop:
            fruits.draw(WIN)

        player.draw(WIN)

        pygame.display.update()

    while running:
        clock.tick(FPS)
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player.get_width() < WIDTH // 2:
            player.x += player_vel


main()
