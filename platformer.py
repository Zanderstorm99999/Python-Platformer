import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Zanderformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
   
    def __init__(self, x, y, image_width, image_height):
        self.rect = pygame.Rect(x, y, image_width, image_height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, image_width, image_height = image.get_rect()
    tiles = []

    for i in range(WIDTH // image_width + 1):
        for j in range(HEIGHT // image_height + 1):
            pos = (i * image_width, j * image_height)
            tiles.append(pos)

    return tiles, image


def draw(window, tiles, bg_image, player):
    for tile in tiles:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    tiles, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        draw(window, tiles, bg_image, player)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
