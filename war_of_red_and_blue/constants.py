import pygame
import os


# Fontları kullanmak için gerekli
pygame.font.init()


# Ses eklemek için gerekli
pygame.mixer.init()


# Ekran ayarları
WIDTH, HEIGHT = 1100, 600

# Pencere oluştur
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Pencere başlığı
pygame.display.set_caption("War of Red and Blue")


# RENKLER

# Askerlerle ilişiği olan renkler
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#  Diğer renklerle kontrast oluşturuyor: RED üzerine yazı yazarken vb.
WHITE = (255, 255, 255)

# Rengin henüz RED ya da BLUE olmadığı durumda kullanılır
BLACK = (0, 0, 0)

# Fontlar
HEALTH_FONT = pygame.font.SysFont('verdana', 24)
WINNER_FONT = pygame.font.SysFont('verdana', 48)


# FPS
FPS = 50


# Asker ve mermi hızları
VELOCITY = 6 # asker hızı
BULLET_VELOCITY = 6 # mermi hızı


# Aynı anda atılabilecek mermi sayısı
MAX_BULLETS = 5


# Asker boyutları
SOLDIER_WIDTH = 55
SOLDIER_HEIGHT = 60


# Olaylar
RED_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2


# Kırmızı asker görseli
RED_SOLDIER_IMAGE = pygame.image.load(
    os.path.join('assets', 'red_soldier.png'))
RED_SOLDIER = pygame.transform.rotate(pygame.transform.scale(
    RED_SOLDIER_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT)), 0)


# Mavi asker görseli
BLUE_SOLDIER_IMAGE = pygame.image.load(
    os.path.join('assets', 'blue_soldier.png'))
BLUE_SOLDIER = pygame.transform.rotate(pygame.transform.scale(
    BLUE_SOLDIER_IMAGE, (SOLDIER_WIDTH, SOLDIER_HEIGHT)), 0)


# Arkaplan görseli
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'background.png')), (WIDTH, HEIGHT))


# Oyun simgesi
ICON = pygame.image.load(os.path.join('assets', 'game_icon.png'))
pygame.display.set_icon(ICON)


# Mermi sesi
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join('assets', 'bullet_sound.mp3'))
