import pygame.math

from package.body import *

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Game:
    def __init__(self):
        pygame.init()

        self.start_time = pygame.time.get_ticks()

        self.camera_pos = pygame.math.Vector2(0,0)
        self.magnification = 2
        self.dt = 150

        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.planet = Body(200, 100, 100, 10)
        self.planet2 = Body(200, 200, 10000000, 50)
        self.planet3 = Body(400, 400, 10000, 25)
        planets.add(self.planet)
        planets.add(self.planet2)
        planets.add(self.planet3)

    def draw(self):
        self.screen.fill(BLACK)
        self.planet.draw(self.screen, self.camera_pos, self.magnification, self.dt)
        self.planet2.draw(self.screen, self.camera_pos, self.magnification, self.dt)
        self.planet3.draw(self.screen, self.camera_pos, self.magnification, self.dt)
        pygame.display.flip()

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.camera_pos.y -= 5
        if keys[pygame.K_s]:
            self.camera_pos.y += 5
        if keys[pygame.K_a]:
            self.camera_pos.x -= 5
        if keys[pygame.K_d]:
            self.camera_pos.x += 5

        if keys[pygame.K_UP]:
            self.magnification += 0.1
        if keys[pygame.K_DOWN]:
            self.magnification -= 0.1

        if keys[pygame.K_MINUS]:
            self.dt -= 20
        if keys[pygame.K_PLUS]:
            self.dt += 20

        if pygame.time.get_ticks() - self.start_time <= 3000:
            self.planet.set_forces(pygame.math.Vector2(0.00001,0))
            self.planet2.set_forces(pygame.math.Vector2(0.02, 0))
            self.planet3.set_forces(pygame.math.Vector2(0.0004, -0.0004))

        self.planet.update(self.dt, planets)
        self.planet2.update(self.dt, planets)
        self.planet3.update(self.dt, planets)

    def loop(self):
        while True:
            events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.loop()
