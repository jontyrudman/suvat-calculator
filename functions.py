from math import sqrt

#SUVAT function names should in the format:
#return_have
#This means if we want v but have u,a,t it would be v_uat
#The have section's letters must be in the order of "suvat"
#The order of the paramaters must also follow the order of "suvat"

#v=u+at
def v_uat(u:float, a:float, t:float) -> float:
	return float(u + (a*t))

def u_vat(v:float, a:float, t:float) -> float:
	return float(v - (a * t))

def t_uva(u:float, v:float, a:float) -> float:
	return float((v - u)/ a)

def a_uvt(u:float, v:float, t:float) -> float:
	return float((v - u)/ t)

#s=u+0.5at^2
def s_uat(u:float, a:float, t:float) -> float:
	return float(u + (0.5 * a * t**2))

def u_sat(s:float, a:float, t:float) -> float:
	return float(s-(0.5 * a * t**2))

def a_sut(s:float, u:float, t:float) -> float:
	return float((2 * (s - u))/t**2)

def t_sua(s:float, u:float, a:float) -> float:
	return float(math.sqrt((2*(s-u))/a))

#s=v-0.5at^2
def s_vat(v:float, a:float, t:float) -> float:
	return float(v - (0.5 * a * t**2))

def v_sat(s:float, a:float, t:float) -> float:
	return float(s+(0.5 * a * t**2))

def a_svt(s:float, v:float, t:float) -> float:
	return float((2 * (v - s))/ t**2)

def t_sva(s:float, v:float, a:float) -> float:
	return float(math.sqrt((2 * (v - s))/ a))

#v^2=u^2+2as
def v_sua(s:float, u:float, a:float) -> float:
	return float(math.sqrt(u**2 + 2 * a * s))

def u_sva(s:float, v:float, a:float) -> float:
	return float(math.sqrt(v**2 - 2 * a *s))

def a_suv(s:float, u:float, v:float) -> float:
	return float((v**2 - u**2)/ (2 * s))

def s_uva(u:float, v:float, a:float) -> float:
	return float((v**2 - u**2)/ (2 * a))

#s=t(u+v)/2
def s_uvt(u:float, v:float, t:float) -> float:
	return float(((u + v)/ 2) * t)

def u_svt(s:float, v:float, t:float) -> float:
	return float(((2 * s)/ t) - v)

def v_sut(s:float, u:float, t:float) -> float:
	return float(((2 * s)/ t) - u)

def t_suv(s:float, u:float, v:float) -> float:
	return float((2 * s)/ (u + v))

#Old eqs
def tx_equals_2sx_over_ux_plus_vx(s, u, v):
    t = (2 * float(s)) / (float(u) + float(v))
    return t

def tx_equals_sx_over_ux(s, u):
    t = float(s)/float(u)
    return t

def ty_equals_minus_uy_over_ay(u, a):
    t = (-float(u))/float(a)
    return t

def ty_equals_2_times_sy_over_uy(s, u):
    t = (2*float(s))/float(u)
    return t

def sx_equals_ux_times_tx(u, t):
    s = float(u)*float(t)
    return s

def sy_equals_minus_uy_squared_over_2_times_ay(u, a):
    s = -(float(u)**2)/(2*float(a))
    return s

def sy_equals_ut_plus_half_a_times_t_squared(u, t, a):
    s = (float(u)*float(t))+(0.5*float(a)*(float(t)**2))
    return s

def sy_equals_vt_minus_half_a_times_t_squared(t, a):
    s = -(0.5*float(a)*(float(t)**2))
    return s

def uy_equals_sqrt_vy_squared_minus_2aysy(a, s):
    u = sqrt(-2*(float(a)*float(s)))
    return u

def uy_equals_vy_minus_ay_times_ty(a, t):
    u = -(float(a)*float(t))
    return u

def uy_equals_sy_minus_half_ay_ty_sq_over_ty(s, a, t):
    u = (float(s)-(0.5*float(a)*(float(t)**2)))/float(t)
    return u

def uy_equals_2sy_over_ty_minus_vy(s, t):
    u = (2*float(s))/float(t)
    return u

def ux_equals_sx_over_tx(s, t):
    u = float(s)/float(t)
    return u

def ay_equals_minus_uy_sq_over_2sy(u, s):
    a = -(float(u)**2)/(2*float(s))
    return a

def ay_equals_minus_uy_over_ty(u, t):
    a = (-float(u))/float(t)
    return a

def ay_equals_2_times_sy_minus_uyty_over_ty_sq(s, u, t):
    a = (2*(float(s)-(float(u)*float(t))))/(float(t)**2)
    return a

def ay_equals_minus_2_times_sy_minus_vyty_over_ty_sq(s, t):
    a = (-2*(float(s)))/(float(t)**2)
    return a
