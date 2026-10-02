from package import *

def calc_f_gravitation(body, other, body_pos):
    offset = other.get_pos() - body_pos
    distance = offset.length()

    if distance < 10e-6:
        return pygame.math.Vector2(0,0)

    unit_vec = offset / distance
    f_gravitational = ((GRAV_CONST * other.get_mass() * body.get_mass()) / distance ** 2) * unit_vec
    return f_gravitational

def calc_acceleration(object_force, object_mass):
    return object_force / object_mass