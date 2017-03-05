import functions

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

    elif "" not in (s, u, a):
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
