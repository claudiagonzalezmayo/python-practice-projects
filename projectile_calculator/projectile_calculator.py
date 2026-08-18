import math
GRAVITY= 9.81
def main():
    while True:
        try:
            velocity= (float(input("Please introduce the velocity of the projectile in m/s: ")))
            print()
            angle=(float(input("Please introduce the angle of the projectile respect of the ground in degrees: ")))
            print()
            print("....................................................................................................")
            print()
            vertical_component, horizontal_component= calculate_velocity_components(velocity, angle)
            time_of_flight= flight_time(vertical_component)
            print(f"The flight time of this projectile is {time_of_flight: .2f} seconds")
            print()
            max_altitude= maximum_altitude(vertical_component)
            print(f"The maximum altitude the projectile reaches is {max_altitude: .2f} meters")
            print()
            hor_distance= horizontal_distance(horizontal_component, vertical_component)
            print(f"The horizontal distance is {hor_distance: .2f} meters")
            print()
        except ValueError:
            print('Input must be a number')

def calculate_velocity_components(velocity, angle):

    vertical_component= velocity*math.sin(math.radians(angle))
    horizontal_component=velocity*math.cos(math.radians(angle))
    return vertical_component, horizontal_component

def flight_time(vertical_velocity ):
    time_of_flight= 2* vertical_velocity/GRAVITY
    return time_of_flight
def maximum_altitude(vertical_velocity):
    height= (vertical_velocity**2)/(2*GRAVITY)
    return height
def horizontal_distance(horizontal_velocity, vertical_velocity):
    horizontal_distance= horizontal_velocity*flight_time(vertical_velocity)
    return horizontal_distance
main()