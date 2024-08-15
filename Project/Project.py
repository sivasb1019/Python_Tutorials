import time
while(True):
    User=input("Enter your mode(Manualmode or Automode):")
    a=1
    if(User=="Manualmode"):
        while(a!=0):
            Direction=input("Enter Direction:")
              
            if(Direction=="west" or Direction=="West" ):
                print("Green light in West")
                print("Orange light in East")
                print("Red light in North")
                print("Red light in South")
                print()
               

            elif(Direction=="east" or Direction=="East"):
                print("Green light in East")
                print("Orange light in West")
                print("Red light in North")
                print("Red light in South")
                print()
                

            elif(Direction=="north" or Direction=="North"):
                print("Green light in North")
                print("Orange light in South")
                print("Red light in East")
                print("Red light in West")
                print()
                
            elif(Direction=="south" or Direction=="South"):
                print("Green light in South")
                print("Orange light in North")
                print("Red light in East")
                print("Red light in West")
                print()
               
            else:
                print("Invalide Data")
                break
            a+=1
    elif(User=="Automode"):
        n=1
        m=int(input("How many times automode need to run?:"))
        t=int(input("enter time gap:"))
        while(n<=m):
            print("Green light in West")
            print("Orange light in East")
            print("Red light in North")
            print("Red light in South")   
            print()
            time.sleep(t)
            print("Green light in East")
            print("Orange light in West")
            print("Red light in North")
            print("Red light in South")
            print()
            time.sleep(t)
            print("Green light in North")
            print("Orange light in South")
            print("Red light in East")
            print("Red light in West")
            print()
            time.sleep(t)
            print("Green light in South")
            print("Orange light in North")
            print("Red light in East")
            print("Red light in West")
            print()
            time.sleep(t)
            n+=1

    exits=input("Do you want to exit?(yes/no)")
    if(exits== "yes"):
            print("PROGRAM SUCCESSFULLY ENDED")
            break   

                  
                     
       

                                





    
