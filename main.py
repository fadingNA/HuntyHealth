from setting import *
from player import *
from sound import *


def main():
    game_state = "start_menu"
    running = True
    user = "Test User"
    point = 1
    lives = 4
    main_font = pygame.font.SysFont("comicsans", 36)
    lost_font = pygame.font.SysFont("comiccons", 50)
    menu_start_font = pygame.font.SysFont("comiccons", 70)
    player = Player(300, 550)
    player_vel = 6
    # Enemy Init
    fruit_drop = []
    wave_length = 3
    fruit_drop_vel = 1
    lost = False
    lost_count = 0
    fruit_count = 0

    def draw_start_menu():
        WIN.blit(BG_start_game, (0, 0))
        title = menu_start_font.render("Healthy Hunt", True, (255, 255, 255))
        start_button = menu_start_font.render('Start', True, (255, 255, 255))
        WIN.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 2 - title.get_height() / 2))
        WIN.blit(start_button, (
            WIDTH / 2 - start_button.get_width() / 2, start_button.get_height() / 2 + start_button.get_height() / 2))
        pygame.display.update()

    def draw_window():
        WIN.blit(BG, (0, 0))
        # sidebar
        sidebar = pygame.Surface((100, HEIGHT))
        sidebar.fill((50, 50, 50))
        # draw text
        user_label = main_font.render(f"Username: {user}", 1, (255, 80, 100))
        life_label = main_font.render(f"Life: {lives}", 1, (0, 255, 255))
        point_label = main_font.render(f"Point: {point}", 1, (0, 255, 255))
        next_label = main_font.render(f"Next Ingredient : ", None, (255, 255, 255))
        # Win blit
        WIN.blit(sidebar_img, (WIDTH - sidebar.get_width() - 30, 170))
        WIN.blit(user_label, (10, 10))
        WIN.blit(life_label, (WIDTH - life_label.get_width() - 10, 10))
        WIN.blit(point_label, (WIDTH - point_label.get_width() - 10, 70))
        WIN.blit(next_label, (10, 50))

        fruit_image = {
            "hamburger": playerS_HAMBURGER,
            "tomato": playerS_TOMATOES,
            "cabbage": playerS_CABBAGE,
            "salmonm": playerS_salmon,
            "carrot": playerS_CARROT,
        }
        fruit_x = 10
        fruit_y = 100
        """for i in range(wave_length):
                fruit_d = FruitDrop(random.randrange(50, WIDTH - 100),
                                    random.randrange(-1500, -100),
                                    random.choice(["tomatoes", "carrot", "cabbage", "hamburger"]))
                fruit_drop.append(fruit_d)"""
        fruit_drop_side = []
        for j in range(5):
            fruit_side_bar = FruitDrop(30,70,random.choice(["tomatoes","carrot","cabbage", "hamburger"]))
            fruit_drop_side.append(fruit_side_bar)


        for fruits in fruit_drop:
            fruits.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost !!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    while running:
        clock.tick(FPS)
        if game_state == "start_menu":
            keys = pygame.key.get_pressed()
            draw_start_menu()
            if keys[pygame.K_SPACE]:
                player_x = 200
                player_y = 400
                game_state = "game"
                game_over = False
        if game_state == "game":
            draw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                running = False
            else:
                continue

        if len(fruit_drop) == 0:
            point += 1
            wave_length += 5
            for i in range(wave_length):
                fruit_d = FruitDrop(random.randrange(50, WIDTH - 100),
                                    random.randrange(-1500, -100),
                                    random.choice(["tomatoes", "carrot", "cabbage", "hamburger","corn"]))
                fruit_drop.append(fruit_d)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
            #move_left.play()
        if keys[pygame.K_d] and player.x + player.get_width() < WIDTH:
            player.x += player_vel
            #move_right.play()

        for f in fruit_drop:
            f.move(fruit_drop_vel)

            if collide(f, player):
                point += 1
                collect_sound.play()
                fruit_drop.remove(f)

            if f.y + f.get_height() > HEIGHT:
                lives -= 1
                collect_sound.play()

                fruit_drop.remove(f)


main()
