#Write a code for creating the Traffic light logic.
'''
    Note:
	-Need to select 4 Directions(East,West,North,South)
	-Need to use 3 LEDs(Green,red,Orange - Use print functions instead of LEDs)
	-Need to use 2 modes(Automode,Manual mode)
	-Mode is an input given by user during runtime.
	-In Automode each direction should run 1 minute.
	-In Manualmode get input from the user.

    Name: Siva Balan V
    Email: sivabalansb1019@gmail.com
    Mobile no:8248451858
'''


def auto_mode():
    print()
    n = int(input("How many times automode need to run? "))
    gap = int(input("Enter the time gap between each directions: "))
    print("Each direction will delayed for",gap,"seconds")
    directions = ["East", "North", "West", "South"]
    for i in range(n):
        print(directions[0]," is Green")
        print(directions[1]," is Orange")
        print(directions[2]," is Red")
        print(directions[3]," is Red")
        time.sleep(gap)
        a = directions.pop(0)
        directions.append(a)
        print()
    exit(mode)
        
def manual_mode():
    print()
    direction = input("Enter direction: ")
    print()
    if(direction.lower() == "east"):
        print("East is Green")
        print("North is Orange")
        print("West is Red")
        print("South is Red")
        manual_mode()

    elif(direction.lower() == "north"):
        print("North is Green")
        print("West is Orange")
        print("South is Red")
        print("East is Red")
        manual_mode()

    elif(direction.lower() == "west"):
        print("West is Green")
        print("South is Orange")
        print("East is Red")
        print("North is Red")
        manual_mode()
    
    elif(direction.lower() == "south"):
        print("South is Green")
        print("East is Orange")
        print("North is Red")
        print("West is Red")
        manual_mode()
    
    else:
        print("Invalid data")
        exit(mode)

def exit(mode):
    print()
    option = input("Do you want to exit?(Yes/No): ")
    if(option.lower() == "yes"):
        print("Programs is ended....")
    elif(option.lower() == "no"):
        change = input("Do you wan to change the mode?(Yes/No): ")
        if(change.lower() == "yes"):
            mode = input("Enter mode(Manualmode or Automode): ")
            print()
            if(mode.lower() == "automode"):
                print("Automode is activated...")
                auto_mode()
            elif(mode.lower() == "manualmode"):
                print("Manualmode is activated...")
                manual_mode()
            else:
                print("Invalid mode type")
                exit(mode)
        elif(change.lower() == "no"):
            print()
            if(mode.lower() == "automode"):
                print("Automode is activated...")
                auto_mode()
            else:
                print("Manualmode is activated...")
                manual_mode()
        else:
            print("Invalid option, Enter valid option(Yes/No)....")
            exit(mode)
    else:
        print("Invalid option, Enter valid option(Yes/No)....")
        exit()

import time
global mode
mode = input("Enter mode(Manualmode or Automode): ")
print()
if(mode.lower() == "automode"):
    print("Automode is activated...")
    auto_mode()
        
elif(mode.lower() == "manualmode"):
    print("Manualmode is activated...")
    manual_mode()
else:
    print("Invalid mode type")
    exit(mode)
