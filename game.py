import pygame
import time
from player_ship import PlayerShip
from alien_ship import AlienShip
from alien_laser import AlienLaser


def game_loop(window, width, height):
    # Your game initialization code here
    player = PlayerShip(250, 650, "player.jpeg")
    player.resize_image(100, 100)

    alien_list = []
    for i in range(3):
        alien = AlienShip(100 * i + i * 50, 50, "alien.jpeg")
        alien.resize_image(100, 100)
        alien_list.append(alien)

    alien_speed = 50
    alien_lasers = []
    laser_speed = 5
    laser_time = 60

    running = True
    game_over = False
    score = 0

    clock = pygame.time.Clock()
    frame_count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if not game_over:
            player.update_position(keys, width)

            window.fill((0, 0, 0))

            dt = clock.tick(60) / 1000.0
            frame_count += 1

            for alien in alien_list:
                alien.move(dt)
                if alien.at_edge(width):
                    alien.change_direction()

                alien.draw(window)

            player.draw(window)

            if frame_count % laser_time == 0:
                alien_speed += 5
                if laser_time > 0.5:
                    laser_time -= 0.5
                for alien in alien_list:
                    laser = AlienLaser(alien.x + 50, alien.y + 50)
                    alien_lasers.append(laser)
                    alien.set_speed(alien_speed)

            for laser in alien_lasers[:]:
                laser.move(laser_speed)
                if laser.y > height:
                    alien_lasers.remove(laser)

            for laser in alien_lasers:
                laser.draw(window)

            for laser in alien_lasers[:]:
                laser_rect = pygame.Rect(laser.x, laser.y, laser.width, laser.height)
                player_rect = pygame.Rect(player.x, player.y, 100, 100)

                if laser_rect.colliderect(player_rect):
                    game_over = True

            score = frame_count // 50

            frame_text = pygame.font.SysFont("Arial", 24).render("Score: " + str(score), True, (255, 255, 255))
            window.blit(frame_text, (10, 10))

        else:
            game_over_text = pygame.font.SysFont("Arial", 36).render("You Died", True, (255, 255, 255))
            score_text = pygame.font.SysFont("Arial", 24).render("Final Score: " + str(score), True, (255, 255, 255))

            window.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 3))
            window.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))

            pygame.display.update()
            time.sleep(3)
            running = False

        pygame.display.update()

    pygame.quit()
    quit()
