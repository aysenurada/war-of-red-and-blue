import pygame
from constants import *
from soldier import Soldier
from utils import draw_window, draw_winner


def main():
    # Kırmızı ve mavi askerleri oluştur
    red = Soldier(200, 420, SOLDIER_WIDTH, SOLDIER_HEIGHT, RED_SOLDIER)
    blue = Soldier(840, 425, SOLDIER_WIDTH, SOLDIER_HEIGHT, BLUE_SOLDIER)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Farklı sistemler için (Windows, Mac, Linux)
                # farklı tuşlar kullanılabilir:
                # K_LCTRL: sol CTRL tuşu, K_LMETA: Mac command tuşu gibi

                # Kırmızı asker mermi ateşler.
                if event.key in [pygame.K_LCTRL, pygame.K_LMETA] and len(red.bullets) < MAX_BULLETS:
                    BULLET_FIRE_SOUND.play()
                    bullet = pygame.Rect(
                        red.rect.x + red.rect.width, red.rect.y + red.rect.height // 2 - 2, 10, 5)
                    red.bullets.append(bullet)

                # Mavi asker mermi ateşler
                if event.key in [pygame.K_RCTRL, pygame.K_RMETA] and len(blue.bullets) < MAX_BULLETS:
                    BULLET_FIRE_SOUND.play()
                    bullet = pygame.Rect(
                        blue.rect.x, blue.rect.y + blue.rect.height // 2 - 2, 10, 5)
                    blue.bullets.append(bullet)

            # Kırmızı asker vurulduysa
            if event.type == RED_HIT:
                # Kırmızı askerin canını azalt
                red.health -= 1

            # Mavi asker vurulduysa
            if event.type == BLUE_HIT:
                # Mavi askerin canını azalt
                blue.health -= 1

        # Kazananı belirleme
        winner_text = ""
        winner_color = BLACK

        # Kırmızı asker kazanırsa
        if blue.health <= 0:
            winner_text = "Red Soldier Wins!"
            winner_color = RED

        # Mavi asker kazanırsa
        elif red.health <= 0:
            winner_text = "Blue Soldier Wins!"
            winner_color = BLUE

        # Kazanan varsa
        if winner_text != "":
            draw_winner(winner_text, winner_color)  # Kazananı göster
            break  # Oyunu bitir

        # Basılı tuşları al
        keys_pressed = pygame.key.get_pressed()

        # Kırmızı askeri hareket ettir
        red.move(keys_pressed, pygame.K_a, pygame.K_d,
                 pygame.K_w, pygame.K_s, (0, WIDTH // 2 - 5))

        # Mavi askeri hareket ettir
        blue.move(keys_pressed, pygame.K_LEFT, pygame.K_RIGHT,
                  pygame.K_UP, pygame.K_DOWN, (WIDTH // 2 + 5, WIDTH))

        # Kırmızı askerin mermilerini yönet
        red.handle_bullets(blue)

        # Mavi askerin mermilerini yönet
        blue.handle_bullets(red)

        # Ekranı güncelle
        draw_window(red, blue)

    main()  # Oyunu bitince tekrar başlat
