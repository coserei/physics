from package.planet import *

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.planet = Planet(100,100)
        self.planet2 = Planet(200, 200)
        planets.add(self.planet)
        planets.add(self.planet2)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.planet.draw(self.screen)
        self.planet2.draw(self.screen)
        pygame.display.flip()

    def update(self):
        self.planet.update()
        self.planet2.update()

    def loop(self):
        while True:
            events()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.loop()
