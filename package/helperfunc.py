from package import *

def calc_f_gravitation(object, other_object):
    object_pos = object.get_pos()
    object_mass = object.get_mass()

    object2_mass = other_object.get_mass()
    object2_pos = other_object.get_pos()

    distance = math.sqrt((object2_pos.y - object_pos.y) ** 2 + (object2_pos.x - object_pos.x) ** 2)

    unit_vec = pygame.math.Vector2(0,0)
    unit_vec.x = object2_pos.x - object_pos.x
    unit_vec.y = object2_pos.y - object_pos.y
    unit_vec = unit_vec / distance

    f_gravitational = ((GRAV_CONST * object2_mass * object_mass) / distance ** 2) * unit_vec

    return f_gravitational

def calc_acceleration(object_force, object_mass):
    # CHANGE: Should actually be sum of all forces (Fnet) divided by total mass.

    acceleration = pygame.math.Vector2(0,0)
    acceleration.x = object_force.x / object_mass
    acceleration.y = object_force.y / object_mass

    print(acceleration)
    return acceleration

def calc_distance_to_object(object):
    planets = []
    for other_object in planets:
        dx = other_object.pos.x - object.pos.x
        dy = other_object.pos.y - object.pos.y
        distance = math.sqrt(dx**2+dy**2)


