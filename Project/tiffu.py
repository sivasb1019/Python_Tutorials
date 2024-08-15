def automode():
        import time 
        direction=["east","north","west","south"]
        times=int(input("How many time signal want to run:"))
        for i in range(len(direction)*times):
           print(direction[0],"is green")
           print(direction[1],"is orange")
           print(direction[2],"is red")
           print(direction[3],"is red")
           time.sleep(3)
           print()
           x=direction.pop(0)
           direction.append(x)
def manualmode():
        direction=(input("Enter the direction:")).lower()
        if(direction=="west"):
           print("West is Green")
           print("South is orange")
           print("East is red")
           print("North is red")
           manualmode()
        elif(direction=="north"):
            print("North is Green")
            print("East is orange")
            print("South is red")
            print("West is red")
            manualmode()
        elif(direction=="south"):
            print("South is Green")
            print("West is orange")
            print("North is red")
            print("East is red")
            manualmode()
        elif(direction=="east"):
            print("East is Green")
            print("North is orange")
            print("South is red")
            print("West is red")
            manualmode()
        else:
            print("invalid direction")
                   
          
mode=input("Enter the mode Automode OR Manualmode:").lower()
if(mode=="manualmode"):
    manualmode()
   
        
elif(mode=="automode"):
    automode()
   
else:
    print("invalid mode")
