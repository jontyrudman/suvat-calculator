from validator import *

while True:
    try:
        print("Welcome to the suvat solver! (Currently only works on flat ground)\n")

        print("Please enter x values for this instance of time - leave blank if unknown")
        sx = input("s = ")
        ux = input("u = ")
        vx = input("v = ") #This will be the velocity at this instance of time
        ax = input("a = ")

        print("\nPlease enter y values for this instance of time - leave blank if unknown")
        sy = input("s = ")
        uy = input("u = ")
        vy = input("v = ") #This will be the velocity at this instance of time
        ay = input("a = ")

        print("\nPlease enter the time of this instance occured - leave blank if unknown")
        t = input("t = ") #The point in time from the projectile being released to this instance in time


        suvatInstance = menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, t)
        if suvatInstance == False:
            print("\n"*10, "Invalid. Got any more values? Trying again...\n")
            continue
        else:
            #This is just temporary until we move the suvat stuff into its own class
            sx = suvatInstance[0]
            ux = suvatInstance[1]
            vx = suvatInstance[2]
            ax = suvatInstance[3]
            sy = suvatInstance[4]
            uy = suvatInstance[5]
            vy = suvatInstance[6]
            ay = suvatInstance[7]
            t = suvatInstance[8]
            printSUVATComponents(sx, ux, vx, ax, sy, uy, vy, ay, t)
            break

    except ValueError:
        print("\n"*10, "Please enter numerical values. Trying again...\n")
        continue
input("Press any key to continue")
