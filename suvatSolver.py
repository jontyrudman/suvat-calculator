import functions

#Returns [s, u, v, a, t]
def suvatSolver(s, u, v, a, t):
    #First check 3 values are present as suvat requires 3 values to calc another
    valuesGot = 0
    if s != "":
        valuesGot += 1
    if u != "":
        valuesGot += 1
    if v != "":
        valuesGot += 1
    if a != "":
        valuesGot += 1
    if t != "":
        valuesGot += 1
   
    if valuesGot < 3:
        return False

    #Then go through each one and call the respective function to calc it
    if s == "":
        s = findS(u, v, a, t)
    if u == "":
        u = findU(s, v, a, t)
    if v == "":
        v = findV(s, u, a, t)
    if a == "":
        a = findA(s, u, v, t)
    if t == "":
        t = findT(s, u, v, a)

    return [s, u, v, a, t]

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
