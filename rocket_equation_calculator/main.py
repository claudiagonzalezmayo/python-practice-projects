import calculations
def main():
    while True:
        print("==============================================")
        print('IDEAL DELTA-V FOR A ROCKET CALCULATOR\n1.What does this calculator do?\n2.Perform a calculation\n3.Exit')
        print("==============================================")
        try:
            options=int(input('Select an option: '))
            print("")
        except ValueError:
            print('Please enter a number')
            print()
            continue
        match options:
            case 1:
                print('This calculator is used to calculate how much velocity change can a rocket achieve given a specific amount of propellent using the Tsiolkvosky equation.')
                print('.................................................................................')
                print("The initial mass is the rocket's mass before burning the propellent and the final mass after the propellent has been burnt. The exhaust velocity describes how fast the exhaust is expelled relative to the rocket.")
                print('.................................................................................')
                if decision():
                    continue
                else:
                    print("Thank you for using our program!")
                    break
            case 2:
                while True:
                    initial_mass= get_number('Please enter the initial mass in kg: ', minimum= 0, exclusive= True)
                    final_mass= get_number('Please enter the final mass in kg: ', minimum= 0, exclusive= True)
                    
                    if final_mass >= initial_mass:
                        print("The final mass must be less than the initial mass.")
                        continue
                    exhaust_velocity= get_number('Please enter the exhaust velocity in m/s: ', minimum=0, exclusive= True)
                    print(calculations.rocket_delta_v(initial_mass, final_mass, exhaust_velocity))
                    if decision():
                        break
                    else:
                        print("Thank you for using our program!")
                        break            
            case 3:
                print('Thank you for using our program!')
                break
            case _:
                print('Please select a valid output')

def decision():
    while True:
        try:
            decision= str(input('Would you like to perform another calculation? (y/n): '))
            print()
        except ValueError:
            print('Please enter a valid input (y/n)')
        if decision=='y':
            return True
        if decision == 'n':
            return False
        else:
            print('Invalid option!')

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
main()

