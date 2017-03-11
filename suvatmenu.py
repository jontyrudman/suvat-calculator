from validator import menuvalidator

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

		# If menuvalidator() returns False, tell the user their input
		# configuration is invalid.
		if menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, t) == False:

			print("\n"*10, "Invalid. Got any more values? Trying again...\n")
			continue
		else:
			break

	except ValueError:
		print("\n"*10, "Please enter numerical values. Trying again...\n")
		continue
input("Press any key to continue")
