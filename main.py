import pygame
from menu import draw_menu
from game import game_loop


def main():
    pygame.init()
    width, height = 600, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Space Evader")

    menu_result = draw_menu(window, width, height)

    if menu_result == 0:
        game_loop(window, width, height)

    pygame.quit()


if __name__ == "__main__":
    main()
