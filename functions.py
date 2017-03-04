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
