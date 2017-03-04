import functions
import math

# Validates the values inputted by sending them to
    # the correct function and returning True.
def menuvalidator(sx, sy, ux, uy, vx, vy, ax, ay, tx, ty):
    
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
    last_conditions_unmet = 6
    conditions_unmet = 0
    while True:

        if sx == "":

            if "" not in (ux, ax, tx):
                sx = functions.s_uat(ux, ax, tx)

            elif "" not in (vx, ax, tx):
                sx = functions.s_vat(vx, ax, tx)

            elif "" not in (ux, vx, ax):
                sx = functions.s_uva(ux, vx, ax)

            elif "" not in (ux, vx, tx):
                sx = functions.s_uvt(ux, vx, tx)

            else: conditions_unmet += 1

        if sy == "":

            if "" not in (uy, ay, ty):
                sy = functions.s_uat(uy, ay, ty)

            elif "" not in (vy, ay, ty):
                sy = functions.s_vat(vy, ay, ty)

            elif "" not in (uy, vy, ay):
                sy = functions.s_uva(uy, vy, ay)

            elif "" not in (uy, vy, ty):
                sy = functions.s_uvt(uy, vy, ty)

            else: conditions_unmet += 1

        if ux == "":

            if "" not in (vx, ax, tx):
                ux = functions.u_vat(vx, ax, tx)

            elif "" not in (sx, ax, tx):
                ux = functions.u_sat(sx, ax, tx)

            elif "" not in (sx, vx, ax):
                ux = functions.u_sva(sx, vx, ax)

            elif "" not in (sx, vx, tx):
                ux = functions.u_svt(sx, vx, tx)

            else: conditions_unmet += 1

        if uy == "":

            if "" not in (vy, ay, ty):
                uy = functions.u_vat(vy, ay, ty)

            elif "" not in (sy, ay, ty):
                uy = functions.u_sat(sy, ay, ty)

            elif "" not in (sy, vy, ay):
                uy = functions.u_sva(sy, vy, ay)

            elif "" not in (sy, vy, ty):
                uy = functions.u_svt(sy, vy, ty)

            else: conditions_unmet += 1

        if vx == "":

            if "" not in (ux, ax, tx):
                vx = functions.v_uat(ux, ax, tx)

            elif "" not in (sx, ax, tx):
                vx = functions.v_sat(ax, ax, tx)

            elif "" not in (sx, ux, ax):
                vx = functions.v_sua(sx, ux, ax)

            elif "" not in (sx, ux, tx):
                vx = functions.v_sut(sx, ux, tx)

            else: conditions_unmet += 1

        if vy == "":

            if "" not in (uy, ay, ty):
                vy = functions.v_uat(uy, ay, ty)

            elif "" not in (sy, ay, ty):
                vy = functions.v_sat(ay, ay, ty)

            elif "" not in (sy, uy, ay):
                vy = functions.v_sua(sy, uy, ay)

            elif "" not in (sy, uy, ty):
                vy = functions.v_sut(sy, uy, ty)

            else: conditions_unmet += 1

        if ax == "":

            if "" not in (ux, vx, tx):
                ax = functions.a_uvt(ux, vx, tx)

            elif "" not in (sx, ux, tx):
                ax = functions.a_sut(sx, ux, tx)

            elif "" not in (sx, vx, tx):
                ax = functions.a_svt(sx, vx, tx)

            elif "" not in (sx, ux, vx):
                ax = functions.a_suv(sx, ux, vx)

            else: conditions_unmet += 1

        if ay == "":

            if "" not in (uy, vy, ty):
                ay = functions.a_uvt(uy, vy, ty)

            elif "" not in (sy, uy, ty):
                ay = functions.a_sut(sy, uy, ty)

            elif "" not in (sy, vy, ty):
                ay = functions.a_svt(sy, vy, ty)

            elif "" not in (sy, uy, vy):
                ay = functions.a_suv(sy, uy, vy)

            else: conditions_unmet += 1

        if tx == "":

            if "" not in (sx, ux, vx):
                tx = functions.t_suv(sx, ux, vx)

            elif "" not in (ux, vx, ax):
                tx = functions.t_uva(ux, vx, ax)

            elif "" not in (sx, vx, ax):
                tx = functions.t_sva(sx, vx, ax)

            elif "" not in (sx, ux, ax):
                tx = functions.t_sua(sx, ux, ax)

            else: conditions_unmet += 1

        if ty == "":

            if "" not in (sy, uy, vy):
                ty = functions.t_suv(sy, uy, vy)

            elif "" not in (uy, vy, ay):
                ty = functions.t_uva(uy, vy, ay)

            elif "" not in (sy, vy, ay):
                ty = functions.t_sva(sy, vy, ay)

            elif "" not in (sy, uy, ay):
                ty = functions.t_sua(sy, uy, ay)

            else: conditions_unmet += 1

        if conditions_unmet == 0:
            variables = [round(float(sx), 3), round(float(ux), 3),
                         round(float(ux), 3), 0.0,
                         round(float(tx), 3), round(float(sy), 3),
                         round(float(uy), 3), 0.0,
                         round(float(ay), 3), round(float(ty), 3)]
            print(" "*57, "X")
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format("RANGE",
                          "INITIAL VELOCITY",
                          "FINAL VELOCITY",
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

            print("\n", " "*50, "Y (TO APEX)")
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format("HEIGHT",
                          "INITIAL VELOCITY",
                          "FINAL VELOCITY",
                          "ACCELERATION",
                          "TIME TO APEX"))
            print("-"*116)
            print("| {:^20} | {:^20} | {:^20} | {:^20} | {:^20} |"
                  .format(variables[5],
                          variables[6],
                          variables[7],
                          variables[8],
                          variables[9]))
            print("-"*116)

            return True

        elif conditions_unmet == last_conditions_unmet: return False

        else:
            last_conditions_unmet = conditions_unmet
            conditions_unmet = 0
            continue


