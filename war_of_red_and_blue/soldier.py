import pygame
from constants import *


class Soldier:
    '''
    Bu class, askerlerin özelliklerini ve hareketlerini tanımlar.
    '''

    def __init__(self, x, y, width, height, image):
        '''
        x: askerin x koordinatı
        y: askerin y koordinatı
        width: askerin genişliği
        height: askerin yüksekliği
        image: pygame.Surface, askerin görseli
        '''
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image
        self.bullets = []
        self.health = 10

    def draw(self, window):
        '''
        Askeri ve mermileri ekrana çizer.
        '''
        window.blit(self.image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            # Eğer asker kırmızıysa mermi kırmızı olsun, değilse mavi
            if self.image == RED_SOLDIER:
                pygame.draw.rect(window, RED, bullet)
            else:
                pygame.draw.rect(window, BLUE, bullet)

    def move(self, keys, left, right, up, down, border_limit):
        '''
        Askeri hareket ettirir.
        keys: tuşları ve basılı olup olmadıklarını tutar

        left: sola gitmek için atanmış tuş
        right: sağa gitmek için atanmış tuş
        up: yukarı gitmek için atanmış tuş
        down: aşağı gitmek için atanmış tuş
        border_limit: askerin hareket edebileceği sınırlar
        '''

        if keys[left]:  # Sol tuşa basılmışsa
            if self.rect.x - VELOCITY > border_limit[0]:  # Sınırı geçmiyorsa
                self.rect.x -= VELOCITY

        if keys[right]:  # Sağ tuşa basılmışsa
            # Sınırı geçmiyorsa
            if self.rect.x + VELOCITY + self.rect.width < border_limit[1]:
                self.rect.x += VELOCITY

        if keys[up]:  # Yukarı tuşa basılmışsa
            if self.rect.y - VELOCITY > 0:  # Sınırı geçmiyorsa
                self.rect.y -= VELOCITY

        if keys[down]:  # Aşağı tuşa basılmışsa
            # Sınırı geçmiyorsa
            if self.rect.y + VELOCITY + self.rect.height < HEIGHT - 15:
                self.rect.y += VELOCITY

    def handle_bullets(self, other):
        '''
        Mermileri hareket ettirir ve diğer askere çarptığında olayı tetikler.
        '''
        for bullet in self.bullets:
            # Mermiyi hareket ettir
            if self.image == RED_SOLDIER:
                # Kırmızı asker ise sağa hareket etsin
                bullet.x += BULLET_VELOCITY
            else:
                # Mavi asker ise sola hareket etsin
                bullet.x -= BULLET_VELOCITY

            # Mermi diğer askere çarparsa olayı tetikle
            if other.rect.colliderect(bullet):
                if self.image == BLUE_SOLDIER:
                    pygame.event.post(pygame.event.Event(RED_HIT))
                else:
                    pygame.event.post(pygame.event.Event(BLUE_HIT))
                self.bullets.remove(bullet)

            # Mermi ekran dışına çıkarsa sil
            elif bullet.x > WIDTH or bullet.x < 0:
                self.bullets.remove(bullet)
