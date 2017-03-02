import functions
import math

# Validates the values inputted by sending them to
    # the correct function and returning True.
def menuvalidator(sx, ux, vx, tx, sy, uy, ay, ty):
    
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

        if tx == "":
            if "" not in (sx, ux, vx):
                tx = functions.tx_equals_2sx_over_ux_plus_vx(sx, ux, vx)
                ty = float(tx)/2

            elif "" not in (uy, ay):
                ty = functions.ty_equals_minus_uy_over_ay(uy, ay)
                tx = 2*float(ty)

            elif "" not in (sy, uy):
                ty = functions.ty_equals_2_times_sy_over_uy(sy, uy)
                tx = 2*float(ty)

            elif "" not in (sx, ux):
                tx = functions.tx_equals_sx_over_ux(sx, ux)
                ty = float(tx)/2

            else: conditions_unmet += 1

        if uy == "":
            if "" not in (ay, sy):
                uy = functions.uy_equals_sqrt_vy_squared_minus_2aysy(ay, sy)

            elif "" not in (ay, ty):
                uy = functions.uy_equals_vy_minus_ay_times_ty(ay, ty)

            elif "" not in (sy, ay, ty):
                uy = functions.uy_equals_sy_minus_half_ay_ty_sq_over_ty(sy, ay, ty)

            elif "" not in (sy, ty):
                uy = functions.uy_equals_2sy_over_ty_minus_vy(sy, ty)

            else: conditions_unmet += 1

        if sx == "":
            if "" not in (ux, tx):
                sx = functions.sx_equals_ux_times_tx(ux, tx)

            else: conditions_unmet += 1

        if sy == "":
            if "" not in (uy, ay):
                sy = functions.sy_equals_minus_uy_squared_over_2_times_ay(
                        uy, ay)
            elif "" not in (uy, ty, ay):
                sy = functions.sy_equals_ut_plus_half_a_times_t_squared(
                        uy, ty, ay)
            elif "" not in (ty, ay):
                sy = functions.sy_equals_vt_minus_half_a_times_t_squared(
                        0, ty, ay)

            else: conditions_unmet += 1

        if ux == "":
            if "" not in (sx, tx):
                ux = functions.ux_equals_sx_over_tx(sx, tx)
                vx = ux

            else: conditions_unmet += 1

        if ay == "":
            if "" not in (uy, sy):
                ay = functions.ay_equals_minus_uy_sq_over_2sy(uy, sy)

            elif "" not in (uy, ty):
                ay = functions.ay_equals_minus_uy_over_ty(uy, ty)

            elif "" not in (sy, uy, ty):
                ay = functions.ay_equals_2_times_sy_minus_uyty_over_ty_sq(sy, uy, ty)

            elif "" not in (sy, ty):
                ay = functions.ay_equals_minus_2_times_sy_minus_vyty_over_ty_sq(sy, ty)

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
        elif conditions_unmet == last_conditions_unmet:
            return False

        else:
            last_conditions_unmet = conditions_unmet
            conditions_unmet = 0
            continue


