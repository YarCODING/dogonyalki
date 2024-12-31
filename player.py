import pygame

class PLAYER:
    def __init__(self, x:int, y:int, w:int, h:int, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = image
        self.image = pygame.transform.scale(image, (w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 10


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, size, mode:str):
        keys = pygame.key.get_pressed()

        if mode == 'wasd':
            if keys[pygame.K_d] and self.rect.x < size[0] - self.h:
                self.rect.x += self.speed
            if keys[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.y < size[1] - self.h:
                self.rect.y += self.speed
        elif mode == 'arrows':
            if keys[pygame.K_RIGHT] and self.rect.x < size[0] - self.h:
                self.rect.x += self.speed
            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.y < size[1] - self.h:
                self.rect.y += self.speed




player1_img = pygame.image.load('knight.png')
player2_img = pygame.image.load('ork.png')
player1 = PLAYER(0, 0, 45, 54, player1_img)
player2 = PLAYER(500, 0, 66, 45, player2_img)