import calculations
def main():
    while True:
        print("=================")
        print("ENGINEERING CALCULATOR")
        print()
        print("1.Velocity\n2.Acceleration\n3.Force\n4.Kinetic energy\n5.Potential energy\n6.Exit")
        print("=================")
        try:
            options= int(input("Select an option: "))
            print()
        except ValueError:
            print("Please enter a number: ")
            print()
            continue
        match options:
            case 1:
                distance=get_number("Enter distance(m): ", minimum= 0)
                time=get_number("Enter time (s): ", minimum=0, exclusive= True)
                print(calculations.velocity(distance,time))
                print("....................................................")
                if decision():
                    continue
                else:
                    print('Thank you for using our program!')
                    break
            case 2:
                initial_velocity=get_number("Enter the initial velocity(m/s): ")
                final_velocity=get_number("Enter the final velocity (m/s): ")
                time=get_number("Enter time(s): ", minimum=0, exclusive= True)
                print(calculations.acceleration(initial_velocity, final_velocity, time))
                print("....................................................")
                if decision():
                    continue
                else:
                    print('Thank you for using our program!')
                    break
            case 3:
                mass=get_number("Enter mass(kg) :", minimum= 0, exclusive= True)
                acceleration=get_number("Enter acceleration(m/s**2) :")
                print(calculations.force(mass,acceleration))
                print("....................................................")
                if decision():
                    continue
                else:
                    print('Thank you for using our program!')
                    break
            case 4:
                mass=get_number("Enter mass(kg): " ,minimum= 0,exclusive= True)
                velocity=get_number("enter velocity(m/s): ")
                print(calculations.kinetic_energy(mass, velocity))
                print("....................................................")
                if decision():
                    continue
                else:
                    print('Thank you for using our program!')
                    break
            case 5:
                mass=get_number("Enter mass(kg): ",minimum= 0,exclusive= True)
                height=get_number("Enter height(m): ",minimum= 0)
                print(calculations.potential_energy(mass, height))
                print("....................................................")
                if decision():
                    continue
                else:
                    print('Thank you for using our program!')
                    break
            case 6:
                print('Thank you for using our program!')
                print("....................................................")
                break
            case _:
                print('Invalid option!\n')
def get_number(prompt, minimum= None, exclusive= False):
    while True:
        try:
            variable= float(input(prompt))
            if minimum is not None:
                if exclusive and variable <= minimum:
                    print(f"Value must be greater than {minimum}.")
                    continue
                if not exclusive and variable < minimum:
                    print(f"Value must be at least {minimum}.")
                    continue
            return variable    
        except ValueError:
            print ('Invalid input, must be a number')
def decision():
    while True:
        decision= str(input("Would you like to perform another calculation?(y/n): "))
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print('Invalid input')
        
        

main()