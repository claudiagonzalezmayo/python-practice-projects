def main():
    while True:
        print('====================')
        print("""UNIT CONVERTER\n 1. Distance\n 2. Temperature\n 3. Mass\n 4. Length\n 5. Exit""")
        print('====================')
        print()
        options= int(input("select the option: "))
        print()

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
        print("1 km to miles\n2. miles to km")
        options= int(input('Select the option: '))
        print()
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
    
def mass():
    pass
def length():
    pass
def temperature():
    pass
def decision():
                
                while True:
                    decision= str(input('Would you like to perform another calculation? y/n'))
                    if decision == 'y':
                        return True
                    elif decision == 'n':
                        return False
                    else:
                        print('Invalid option!')

main()