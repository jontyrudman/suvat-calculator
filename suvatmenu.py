from validator import menuvalidator

# Loops the following block until broken, of course.
while True:

	# Try to receive the following inputs. In case of
	# a ValueError, branches to except.
	try:

		# Introduction. Needs work.
		print("Welcome to the suvat solver! (Currently only works on flat ground)\n")

		# Asks for the x values.
		print("Please enter x values for this instance of time - leave blank if unknown")
		sx = input("s = ")
		ux = input("u = ")
		vx = input("v = ") #This will be the velocity at this instance of time
		ax = input("a = ")

		# Asks for the y values.
		print("\nPlease enter y values for this instance of time - leave blank if unknown")
		sy = input("s = ")
		uy = input("u = ")
		vy = input("v = ") #This will be the velocity at this instance of time
		ay = input("a = ")

		print("\nPlease enter the time of this instance occured - leave blank if unknown")
		t = input("t = ") #The point in time from the projectile being released to this instance in time
	
		# If menuvalidator() returns False, tell the user their input
		# configuration is invalid.
		if menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, t) == False:

			print("\n"*10, "Invalid. Got any more values? Trying again...\n")
			continue
		# Otherwise, break out of the loop and finish.
		else: break

	# If there is a ValueError in any of the above inputs,
	# tell the user what was wrong and that it will ask again.
	except ValueError:
		print("\n"*10, "Please enter numerical values. Trying again...\n")
		continue
