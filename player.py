from setting import *


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

    def collect(self):
        if self.counter == 0:
            line = Grap(self.x, self.y, self.player_drop)
            self.line.append(line)
            self.counter = 1

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
        "corn": playerS_CORN
    }

    def __init__(self, x, y, types):
        super().__init__(x, y)
        self.player_img = self.FRUIT_MAP[types]
        self.mask = pygame.mask.from_surface(self.player_img)

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def off_screen(self, height):
        return height >= self.y >= 0


class Grap:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        # self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def offscreen(self, height):
        return height >= self.y >= 0

    def collision(self, obj):
        return collide(self, obj)

    def off_screen(self, height):
        return height >= self.y >= 0

    def collecting(self, obj):
        return collide(self, obj)


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None
