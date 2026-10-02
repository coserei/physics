from package import *
from package.helperfunc import calc_acceleration, calc_f_gravitation

class Body(pygame.sprite.Sprite):
    def __init__(self, x, y, mass, radius):
        super().__init__()

        assert mass > 0
        assert radius > 0

        self.pos = pygame.Vector2(x,y)
        self.forces = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
        self.velocity = pygame.math.Vector2(0, 0)

        self.mass = mass
        self.radius = radius

    def update(self, dt, planets):
        for other_object in planets:
            if other_object != self:
                self.forces += calc_f_gravitation(self, other_object, self.pos)
        self.acc = calc_acceleration(self.forces, self.mass)
        self.velocity += dt * self.acc
        self.pos += dt * self.velocity

        self.forces = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)

    def draw(self, screen, camera_pos, magnification,dt):
        pygame.draw.circle(screen, WHITE,(magnification*(self.pos.x - camera_pos.x), magnification*(self.pos.y - camera_pos.y)),self.radius*magnification)

        proj_pos = self.pos.copy()
        proj_vel = self.velocity.copy()
        proj_forces = self.forces.copy()
        proj_acc = self.acc.copy()
        proj_dt = dt * 10

        for i in range(1000):
            for other_object in planets:
                if other_object != self:
                    proj_forces += calc_f_gravitation(self, other_object, proj_pos)
            proj_acc = calc_acceleration(proj_forces, self.mass)
            proj_vel += proj_dt * proj_acc
            proj_pos += proj_dt * proj_vel

            proj_forces = pygame.math.Vector2(0, 0)
            proj_acc = pygame.math.Vector2(0, 0)
            pygame.draw.circle(screen, (120,120,120), (magnification*(proj_pos.x - camera_pos.x), magnification*(proj_pos.y - camera_pos.y)), 1)

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_pos(self):
        return self.pos

    def set_forces(self, force_x):
        self.forces += force_x

    def __repr__(self):
        return f"Planet({self.pos})"
