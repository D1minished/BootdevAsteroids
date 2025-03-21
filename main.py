import sys
import pygame
from shot import *
from asteroidfield import *
from constants import *
from player import Player


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    
    asteroidfield = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
            
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if obj.check_collision(bullet):
                    bullet.kill()
                    obj.split()
        
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()