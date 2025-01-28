import pygame
from os.path import join
from random import randint

# Player class


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            join("assets", "images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize(
        ) if self.direction else self.direction
        self.rect.center += self.direction * player_speed * dt


# Setup
pygame.init()

# Main setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
running = True
pygame.display.set_caption("Spaceship war")
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Main surface
surf = pygame.Surface((100, 200))
surf.fill("red")
x = 100

# Player
player_surf = pygame.image.load(
    join("assets", "images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

# Stars
star_surf = pygame.image.load(
    join("assets", "images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                  for i in range(20)]

# Meteor
meteor_surf = pygame.image.load(
    join("assets", "images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Laser
laser_surf = pygame.image.load(
    join("assets", "images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

# Initialize instances
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# Game running
while running:
    dt = clock.tick() / 1000

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # recent_keys = pygame.key.get_just_pressed()
    # if recent_keys[pygame.K_SPACE]:
    #     print('laser')

    all_sprites.update(dt)

    # Draw window game
    display_surface.fill("darkgrey")

    # Draw stars
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    # Draw meteor
    display_surface.blit(meteor_surf, meteor_rect)

    # Draw laser
    display_surface.blit(laser_surf, laser_rect)

    # Draw player
    # display_surface.blit(player_surf, player_rect)
    # display_surface.blit(player.image, player.rect)
    all_sprites.draw(display_surface)

    # Update
    pygame.display.update()

pygame.quit()
