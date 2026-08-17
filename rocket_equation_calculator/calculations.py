import math
def rocket_delta_v(initial_mass, final_mass, exhaust_velocity):
    result= exhaust_velocity * math.log(initial_mass/final_mass)
    return f"The delta-v in this rocket is {result: .2f} m/s"