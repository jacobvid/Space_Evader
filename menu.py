import pygame


def draw_menu(window, width, height):
    menu_font = pygame.font.SysFont("Arial", 36)
    title_text = menu_font.render("Space Evader", True, (255, 0, 0))
    start_game_text = menu_font.render("Start Game", True, (255, 255, 255))
    exit_text = menu_font.render("Exit", True, (150, 150, 150))

    selected_option = -1  # Initialize with an invalid option

    menu_running = True

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if width // 2 - start_game_text.get_width() // 2 < mouse_x < width // 2 + start_game_text.get_width() // 2 \
                and (1.5 * height) // 3 < mouse_y < (1.5 * height) // 3 + start_game_text.get_height():
            selected_option = 0

        if width // 2 - exit_text.get_width() // 2 < mouse_x < width // 2 + exit_text.get_width() // 2 \
                and 2 * height // 3 < mouse_y < 2 * height // 3 + exit_text.get_height():
            selected_option = 1

        if pygame.mouse.get_pressed()[0]:
            if selected_option == 0 or selected_option == 1:
                menu_running = False

        window.fill((0, 0, 0))
        window.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 3))
        window.blit(start_game_text, (width // 2 - start_game_text.get_width() // 2, 1.5 * height // 3))
        window.blit(exit_text, (width // 2 - exit_text.get_width() // 2, 2 * height // 3))
        pygame.display.update()

    return selected_option
