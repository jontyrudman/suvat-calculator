from suvatSolver import suvatSolver
import math

This is a test


# Validates the values inputted by sending them to
    # the correct function and returning True.
def menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, t):

   # if uy == "" and "" not in (sy, ay):
    #    uy = functions.u_sva(sy, 0, ay)

    # If ux, uy and ay have values, send them to
        # functions.uxuyay() and return True.
    #if "" not in (ux, uy, ay):
        #functions.uxuyay(ux, uy, ay)
        #return True

    # If sx, sy and ay have values, send them to
        # functions.sxsyay() and return True.
    #elif "" not in (sx, sy, ay):
        #functions.sxsyay(sx, sy, ay)
        #return True


#            if "" not in (sx, ux, vx):
#                t = functions.t_suv(sx, ux, vx)
#
#            elif "" not in (ux, vx, ax):
#                t = functions.t_uva(ux, vx, ax)
#
#            elif "" not in (sx, vx, ax):
#                t = functions.t_sva(sx, vx, ax)
#
#            elif "" not in (sx, ux, ax):
#                t = functions.t_sua(sx, ux, ax)
#
#            else: conditions_unmet += 1

#        if t == "":
#
#            if "" not in (sy, uy, vy):
#                t = functions.t_suv(sy, uy, vy)
#                t = float(2*t)
#
#            elif "" not in (uy, vy, ay):
#                t = functions.t_uva(uy, vy, ay)
#                t = float(2*t)
#
#            elif "" not in (sy, vy, ay):
#                t = functions.t_sva(sy, vy, ay)
#                t = float(2*t)
#
#            elif "" not in (sy, uy, ay):
#                t = functions.t_sua(sy, uy, ay)
#                t = float(2*t)
#
#            else: conditions_unmet += 1


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

            if xComponent[4] == yComponent[4]:
                t = xComponent[4]
            else:
                return False

            variables = [round(float(sx), 3), round(float(ux), 3),
                         round(float(vx), 3), round(float(ax), 3),
                         round(float(t), 3), round(float(sy), 3),
                         round(float(uy), 3), round(float(vy), 3),
                         round(float(ay), 3), round(float(t), 3)]

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
                  .format(variables[0],
                          variables[1],
                          variables[2],
                          variables[3],
                          variables[4]))
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
                  .format(variables[5],
                          variables[6],
                          variables[7],
                          variables[8],
                          variables[9]))
            print("-"*116)

            return
