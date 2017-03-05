import functions
import math

#Returns [sx, ux, vx, ax, sy, uy, vy, ay, t]
def suvatSolver(sx, ux, vx, ax, sy, uy, vy, ay, t):
    last_conditions_unmet = 6
    conditions_unmet = 0
    while True:

        if sx == "":
            sx = findS(ux, vx, ax, t)
            if not isinstance(sx, float):
                conditions_unmet += 1

        if sy == "":
            sy = findS(uy, vy, ay, t)
            if not isinstance(sx, float):
                conditions_unmet += 1

        if ux == "":
            ux = findU(sx, vx, ax, t)
            if not isinstance(ux, float):
               conditions_unmet += 1

        if uy == "":
            uy = findU(sy, vy, ay, t)
            if not isinstance(uy, float):
               conditions_unmet += 1

        if vx == "":
            vx = findV(sx, ux, ax, t)
            if not isinstance(vx, float):
               conditions_unmet += 1

        if vy == "":
            vy = findV(sy, uy, ay, t)
            if not isinstance(vy, float):
               conditions_unmet += 1

        if ax == "":
            ax = findA(sx, ux, vx, t)
            if not isinstance(ax, float):
               conditions_unmet += 1
            
        if ay == "":
            ay = findA(sy, uy, vy, t)
            if not isinstance(vy, float):
               conditions_unmet += 1

        if t == "":
             t = findT(sx, ux, vx, ax)
             if t == "":
                  t = findT(sy, uy, vy, ay)
             else: conditions_unmet += 1

        if conditions_unmet == 0:
             return [sx, ux, vx, ax, sy, uy, vy, ay, t]

        #Return False if no values are found
        elif conditions_unmet == last_conditions_unmet: return False

        else:
            last_conditions_unmet = conditions_unmet
            conditions_unmet = 0
            continue

def findS(u, v, a, t):
    s = ""
    if "" not in (u, a, t):
        s = functions.s_uat(u, a, t)

    elif "" not in (v, a, t):
        s = functions.s_vat(v, a, t)

    elif "" not in (u, v, a):
        s = functions.s_uva(u, v, a)

    elif "" not in (u, v, t):
        s = functions.s_uvt(u, v, t)

    return s

def findU(s, v, a, t):
    u = ""
    if "" not in (v, a, t):
        u = functions.u_vat(v, a, t)

    elif "" not in (s, a, t):
        u = functions.u_sat(s, a, t)

    elif "" not in (s, v, a):
        u = functions.u_sva(s, v, a)

    elif "" not in (s, v, t):
        u = functions.u_svt(s, v, t)

    return u

def findV(s, u, a, t):
    v = ""
    if "" not in (u, a, t):
        v = functions.v_uat(u, a, t)

    elif "" not in (s, a, t):
        v = functions.v_sat(a, a, t)

    elif "" not in (s, u, ax):
        v = functions.v_sua(s, u, a)

    elif "" not in (s, u, t):
        v = functions.v_sut(s, u, t)

    return v

def findA(s, u, v, t):
    a = ""
    if "" not in (u, v, t):
        a = functions.a_uvt(u, v, t)

    elif "" not in (s, u, t):
        a = functions.a_sut(s, u, t)

    elif "" not in (s, v, t):
        a = functions.a_svt(s, v, t)

    elif "" not in (s, u, v):
        a = functions.a_suv(s, u, v)

    return a

def findT(s, u, v, a):
     t = ""
     if "" not in (s, u, v):
        t = functions.t_suv(s, u, v)

     elif "" not in (u, v, a):
        t = functions.t_uva(u, v, a)

     elif "" not in (s, v, a):
        t = functions.t_sva(s, v, a)

     elif "" not in (s, u, a):
        t = functions.t_sua(s, u, a)
     return t

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


        suvatSolved = suvatSolver(sx, ux, vx, ax, sy, uy, vy, ay, t)
        if suvatSolved == False:
             return False
        else:
            sx = suvatSolved[0]
            ux = suvatSolved[1]
            vx = suvatSolved[2]
            ax = suvatSolved[3]
            sy = suvatSolved[4]
            uy = suvatSolved[5]
            vy = suvatSolved[6]
            ay = suvatSolved[7]
            t = suvatSolved[8]
        
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

            return True

        


