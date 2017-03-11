from suvatSolver import suvatSolver
import math

# Validates the values inputted by sending them to
    # the correct function and returning True.
def menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, t):
        xComponent = suvatSolver(sx, ux, vx, ax, t)
        yComponent = suvatSolver(sy, uy, vy, ay, t)

        if xComponent == False or yComponent == False:
             return False
        else:
            sx = xComponent[0]
            ux = xComponent[1]
            vx = xComponent[2]
            ax = xComponent[3]

            sy = yComponent[0]
            uy = yComponent[1]
            vy = yComponent[2]
            ay = yComponent[3]

            #In this section we need to include about trying to recalculate a component if the time can be gained from the other component
            if not isinstance(xComponent[4], float) and isinstance(yComponent[4], float):
                t = yComponent[4]
            elif isinstance(xComponent[4], float) and not isinstance(yComponent[4], float):
                t = xComponent[4]
            elif xComponent[4] == yComponent[4]:
                t = xComponent[4]
            else:
                print(xComponent[4], yComponent[4])
                return False


#            variables = [round(float(sx), 3), round(float(ux), 3),
#                         round(float(vx), 3), round(float(ax), 3),
#                         round(float(t), 3), round(float(sy), 3),
#                         round(float(uy), 3), round(float(vy), 3),
#                         round(float(ay), 3), round(float(t), 3)]

            print(" "*57, "X")
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format("RANGE",
                          "INITIAL VELOCIt",
                          "FINAL VELOCIt",
                          "ACCELERATION",
                          "TOTAL TIME"))
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format(round(float(sx), 3),
                          round(float(ux), 3),
                          round(float(vx), 3),
                          round(float(ax), 3),
                          round(float(t), 3)))
            print("-"*116)

            print("\n", " "*50, "Y")
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format("HEIGHT",
                          "INITIAL VELOCIt",
                          "FINAL VELOCIt",
                          "ACCELERATION",
                          "TIME"))
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format(round(float(sy), 3),
                          round(float(uy), 3),
                          round(float(vy), 3),
                          round(float(ay), 3),
                          round(float(t), 3)))
            print("-"*116)

            return
