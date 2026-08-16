from constants import gravity

def velocity(distance,time):
    result= distance/time
    return f"The final velocity is {result: .2f} m/s"

def acceleration(initial_velocity, final_velocity, time):
    result= (final_velocity-initial_velocity)/time
    return f"The final acceleration is {result: .2f} m/s**2"
def force(mass,acceleration):
    result= mass*acceleration
    return f"The final force is {result: .2f} N"
def kinetic_energy(mass, velocity):
    result= (1/2)*mass*velocity**2
    return f"The final kinetic energy is {result: .2f} J"
def potential_energy(mass, height):
    result= gravity*mass*height
    return f"The final potential energy is {result: .2f} J"