import pygame
from constants import *


def draw_window(red, blue):
    '''
    Pencereyi, skoru ve askerleri çizer.
    '''

    WIN.blit(BACKGROUND, (0, 0))  # Arkaplanı çiz

    # Üst köşelerde kırmızı ve mavi askerlerin canını göster
    red_health_text = HEALTH_FONT.render("Health: " + str(red.health), 1, RED)
    blue_health_text = HEALTH_FONT.render(
        "Health: " + str(blue.health), 1, BLUE)

    WIN.blit(blue_health_text, (WIDTH - blue_health_text.get_width() - 10, 10))
    WIN.blit(red_health_text, (10, 10))

    red.draw(WIN)
    blue.draw(WIN)

    pygame.display.update()


def draw_winner(text, color):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    background_rect = pygame.Rect(WIDTH/2 - draw_text.get_width() / 2 - 20, HEIGHT/2 -
                                  draw_text.get_height()/2 - 20, draw_text.get_width() + 40, draw_text.get_height() + 40)
    pygame.draw.rect(WIN, color, background_rect)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
             2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(3000)  # 3 saniye bekle
