#Write a code for creating the Traffic light logic.
'''
    Note:
	-Need to select 4 Directions(East,West,North,South)
	-Need to use 3 LEDs(Green,red,Orange - Use print functions instead of LEDs)
	-Need to use 2 modes(Automode,Manual mode)
	-Mode is an input given by user during runtime.
	-In Automode each direction should run 1 minute.
	-In Manualmode get input from the user.
'''

import time
mode = input("Enter mode(Manualmode or Automode): ")
if(mode == "automode" or mode == "Automode"):
    directions = ["East","North","West","South"]
    i=0
    for i in range(len(directions)):
        '''
        print(directions[i]," is Green")
        print(directions[i+1]," is Orange")
        print(directions[i+2]," is Red")
        print(directions[i+3]," is Red")
        '''
        if(i==0):
            print("East is Green")
            print("North is Orange")
            print("West is Red")
            print("South is Red")
            time.sleep(10)
            print()
        elif(i==1):
            print("North is Green")
            print("West is Orange")
            print("South is Red")
            print("East is Red")
            time.sleep(10)
        elif(i==2):
            print("West is Green")
            print("South is Orange")
            print("East is Red")
            print("North is Red")
            time.sleep(10)
        elif(i==3):
            print("South is Green")
            print("East is Orange")
            print("North is Red")
            print("West is Red")
            time.sleep(10)
    continue i;
elif(mode == "manualmode" or mode == "Manualmode"):
    direction = input("Enter direction: ")
    if(direction == "East" or direction == "east"):
        print("East is Green")
        print("North is Orange")
        print("West is Red")
        print("South is Red")

    elif(direction == "North" or direction == "North"):
        print("North is Green")
        print("West is Orange")
        print("South is Red")
        print("East is Red")

    elif(direction == "West" or direction == "west"):
        print("West is Green")
        print("South is Orange")
        print("East is Red")
        print("North is Red")
    
    elif(direction == "South" or direction == "South"):
        print("South is Green")
        print("East is Orange")
        print("North is Red")
        print("West is Red")
    else:
        print("Invalid data.... Enter valid direction....");
    
