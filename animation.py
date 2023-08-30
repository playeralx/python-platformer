import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()


class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frames = [pygame.image.load(f'{i}.png').convert_alpha() for i in range(1, 10)]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midleft = (100, 160))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.animation_speed = 0.4
        self.direction = 1

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def move(self):
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        if self.rect.right > 1280 or self.rect.left < 0:
            self.direction *= -1

    def update(self):
        self.animate()
        self.move()

the_group = pygame.sprite.Group()
the_group.add(Animation())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    the_group.update()
    the_group.draw(screen)


    pygame.display.update()
    clock.tick(60)

















































