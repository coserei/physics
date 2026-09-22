from package import *
from package.helperfunc import calc_acceleration, calc_f_gravitation

class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.Vector2(x,y)
        self.forces = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
        self.speed = pygame.math.Vector2(0,0)

        self.mass = 1000
        self.radius = 20

    def update(self):
        for other_object in planets:
            if other_object != self:
                self.forces = calc_f_gravitation(self, other_object)
        self.acc = calc_acceleration(self.forces, self.mass)
        print(self.acc)
        self.speed += self.acc
        self.pos += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.pos.x, self.pos.y),self.radius)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_pos(self):
        return self.pos

    def __repr__(self):
        return f"Planet({self.pos})"
