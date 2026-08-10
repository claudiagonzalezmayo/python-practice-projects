def main():
    while True:
        print('====================')
        print("""UNIT CONVERTER\n 1. Distance\n 2. Temperature\n 3. Mass\n 4. Length\n 5. Exit""")
        print('====================')
        print()
        try:
            options= int(input("select the option: "))
            print()
        except ValueError:
            print("Please enter a number.\n")
            continue 

        match options:
            case 1:
                result= distance()
                print(result, '\n')
                if decision():
                    continue
                else:
                    break
  
            case 2:
                result= temperature()
                print(result, '\n')
                if decision():
                    continue
                else:
                    break
            case 3:
                result= mass()
                print(result, '\n')
                if decision():
                    continue
                else:
                    break
            case 4:
                result= length()
                print(result, '\n')
                if decision():
                    continue
                else:
                    break
            case 5:
                print("Thank you for using our program!")
                break
            case _:
                print("Invalid option\n")
        
    
def distance(): #miles to km km to miles
        print("1. km to miles\n2. miles to km")
        print ()
        try:
            options = int(input("Select the option: "))
            print()
        except ValueError:
            print("Please enter a number.")
            return
        if options == 1:
            value= float(input('You have chosen km-miles: Introduce the distance with just the numbers: '))
            print()
            result= value*0.621371
            return f"The result is {result:.2f} miles"
        elif options == 2:
            value= float(input('You have chosen miles-km: Introduce the distance with just the numbers: '))
            print()
            result= value*1.60934
            return f"The result is {result: .2f} km"
        else:
            print ('Invalid option')
        return

    
def mass(): # kg- lb
    print("1. kg to lb\n2.lb to kg")
    print()
    try:
        options = int(input("Select the option: "))
        print()
    except ValueError:
        print("Please enter a number.")
        return
    if options == 1:
        value= float(input('You have chosen kg-lb: Introduce the weight with just the numbers: '))
        print()
        result= value*2.20462
        return f"The result is {result:.2f} lb"
    elif options == 2:                
        value= float(input('You have chosen lb-kg: Introduce the weight with just the numbers: '))
        print()
        result= value* 0.453592
        return f"The result is {result: .2f} kg"
    else:
        print ('Invalid option')
    return

    
def length(): #m-ft
    print("1. meters to feet\n2.feet to meters")
    print()
    try:
        options = int(input("Select the option: "))
        print()
    except ValueError:
        print("Please enter a number.")
        return
    if options == 1:
        value= float(input('You have chosen meters-feet: Introduce the length with just the numbers: '))
        print()
        result= value* 3.28084
        return f"The result is {result:.2f} ft"
    elif options == 2:                
        value= float(input('You have chosen feet-meters: Introduce the length with just the numbers: '))
        print()
        result= value* 0.3048
        return f"The result is {result: .2f} meters"
    else:
        print ('Invalid option')
    return
    
def temperature(): #Celsius to Fahrenheit 
    print("1.Celsius to Fahrenheit \n2. Fahrenheit to Celsius")
    print()
    try:
        options = int(input("Select the option: "))
        print()
    except ValueError:
        print("Please enter a number.")
        return
    if options == 1:
        value= float(input('You have chosen Celsius to Fahrenheit: Introduce the temperature with just the numbers: '))
        print()
        result= (value * 9/5) + 32
        return f"The result is {result:.2f}°F "
    elif options == 2:                
        value= float(input('You have chosen Fahrenheit to Celsius: Introduce the temperature with just the numbers: '))
        print()
        result= (value-32) * 5/9
        return f"The result is {result: .2f} °C"
    else:
        print ('Invalid option')
    return
def decision():
                
                while True:
                    decision= str(input('Would you like to perform another calculation? y/n: '))
                    print()
                    if decision == 'y':
                        return True
                    elif decision == 'n':
                        return False
                    else:
                        print('Invalid option!')

main()