from validator import menuvalidator

# Loops the following block until broken, of course.
while True:

    # Try to receive the following inputs. In case of
        # a ValueError, branches to except.
    try:

        # Introduction. Needs work.
        print("Welcome to the suvat solver! (Currently only works on flat ground)\n")

        # Asks for the x values.
        sx = input("x: range = ")
        ux = input("   initial velocity = ")

        # If there is no value for initial velocity (ux), ask for vx
            # and set ux to vx.
        if "" == ux:
            vx = input("   final velocity = ")
            if "" not in vx:
                ux = vx
        # Otherwise, set vx to ux.
        else:
            vx = ux
            print("   final velocity =", vx)

        # Notifies the user that x accel is 0.
        print("   acceleration = 0.0")

        # Asks for total time.
        tx = input("   total time = ")

        # Asks for the y values.
        sy = input("\ny: height at apex = ")
        uy = input("   initial velocity = ")

        # Notifies the user that the velocity 
            # at the apex will always be 0.
        print("   velocity at apex = 0.0")
        ay = input("   acceleration = ")

        # If there is no value for total time (tx), ask for ty
            # and set tx as 2*ty.
        if "" == tx:
            ty = input("   time to reach apex = ")
            if "" not in ty:
                tx = 2*float(ty)
        # Otherwise, set ty as half of tx.
        else:
            ty = float(tx)/2
            print("   time to reach apex =", ty)

        # If menuvalidator() returns True, tell the user their input
            # configuration is invalid.
        if menuvalidator(sx, ux, vx, tx, sy, uy, ay, ty) == False:
             print("\n"*10, "Invalid. Got any more values? Trying again...\n")
             continue
        # Otherwise, break out of the loop and finish.
        else: break

    # If there is a ValueError in any of the above inputs,
        # tell the user what was wrong and that it will ask again.
    except ValueError:
        print("\n"*10, "Please enter numerical values. Trying again...\n")
        continue


