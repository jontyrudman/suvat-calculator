from math import sqrt

#SUVAT function names should in the format:
#return_have
#This means if we want v but have u,a,t it would be v_uat
#The have section's letters must be in the order of "suvat"
#The order of the paramaters must also follow the order of "suvat"

def suvatSolver(s, u, v, a, t):
	loops = 0
	while (s = "" or u = "" or v = "" or a = "" or t = "" or s = "Div/0" or u = "Div/0" or v = "Div/0" or a = "Div/0" or t = "Div/0") and loops < 6
		if t = "":
			if "" not in [u, v, a]:
				t = t_uva(u, v, a) #Potential div/0 error
			elif "" not in [s, u, a]:
				t = t_sua(s, u, a)
			elif "" not in [s, v, a):
				t = t_sva(s, v, a)
			elif "" not in [s, u, v]:
				t = t_suv(s, u, v)
		elif s = "":
			if "" not in [u, a, t]:
				s = s_uat(u, a, t)
			elif "" not in [v, a, t]:
				s = s_vat(v, a, t)
			elif "" not in [u, v, a]
				s = s_uva(u, v, a)
			elif "" not in [u, v, t]:
				s = s_uvt(u, v, t)
		elif u = "":
			if "" not in [v, a, t]:
				u = u_vat(v, a, t)
			elif "" not in [s, a, t]:
				u = u_sat(s, a, t)
			elif "" not in [s, v, a]:
				u = u_sva(s, v, a)
			elif "" not in [s, v, t]:
				u = u_svt(s, v, t)
		elif v = "":
			if "" not in [u, a, t]:
				v = v_uat(u, a, t)
			elif "" not in [s, a, t]:
				v = v_sat(s, a, t)
			elif "" not in [s, u, a]:
				v = v_sua(s, v, a)
			elif "" not in [s, u, t]:
				v = v_sut(s, u, t)
		elif a = "":
			print ("Need to do a")

#v=u+at
def v_uat(u:float, a:float, t:float) -> float:
	try:
		u = float(u)
		a = float(a)
		t = float(t)
		return float(u + (a*t))
	except ValueError:
		return "input error"

def u_vat(v:float, a:float, t:float) -> float:
	try:
		v = float(v)
		a = float(a)
		t = float(t)
		return float(v - (a * t))
	except ValueError:
		return "input error"

def t_uva(u:float, v:float, a:float) -> float:
	try:
		u = float(u)
		v = float(v)
		a = float(a)
		return float((v - u)/ a)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def a_uvt(u:float, v:float, t:float) -> float:
	try:
		u = float(u)
		v = float(v)
		t = float(t)
		return float((v - u)/ t)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=ut+0.5at^2
def s_uat(u:float, a:float, t:float) -> float:
	try:
		u = float(u)
		a = float(a)
		t = float(t)
		return float((u*t) + (0.5 * a * t**2))
	except ValueError:
		return "input error"

def u_sat(s:float, a:float, t:float) -> float:
	try:
		s = float(s)
		a = float(a)
		t = float(t)
		return float((s-(0.5 * a * t**2))/t)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def a_sut(s:float, u:float, t:float) -> float:
	try:
		s = float(s)
		u = float(u)
		t = float(t)
		return float((2 * (s - u*t))/t**2)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_sua(s:float, u:float, a:float) -> float:
	try:
		s = float(s)
		u = float(u)
		a = float(a)
		#Disregard the - version of the +- part as t must be positive
		return float((-u + sqrt(u**2 - 2*a*-s))/a)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=vt-0.5at^2
def s_vat(v:float, a:float, t:float) -> float:
	try:
		v = float(v)
		a = float(a)
		t = float(t)
		return float((v*t) - (0.5 * a * t**2))
	except ValueError:
		return "input error"

def v_sat(s:float, a:float, t:float) -> float:
	try:
		s = float(s)
		a = float(a)
		t = float(t)
		return float((s+(0.5 * a * t**2))/t)
	except ValueError:
		return "input error"

def a_svt(s:float, v:float, t:float) -> float:
	try:
		s = float(s)
		v = float(v)
		t = float(t)
		return float((2 * ((v*t) - s))/ t**2)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_sva(s:float, v:float, a:float) -> float:
	try:
		s = float(s)
		v = float(v)
		a = float(a)
		#Disregard the + version of the +- part to get correct answer for t
		return float((v - sqrt(v**2 - 2*a*s))/a)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#v^2=u^2+2as
def v_sua(s:float, u:float, a:float) -> float:
	try:
		s = float(s)
		u = float(u)
		a = float(a)
		return float(sqrt(u**2 + 2 * a * s))
	except ValueError:
		return "input error"

def u_sva(s:float, v:float, a:float) -> float:
	try:
		s = float(s)
		v = float(v)
		a = float(a)
		return float(sqrt(v**2 - 2 * a *s))
	except ValueError:
		return "input error"

def a_suv(s:float, u:float, v:float) -> float:
	try:
		s = float(s)
		u = float(u)
		v = float(v)
		return float((v**2 - u**2)/ (2 * s))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def s_uva(u:float, v:float, a:float) -> float:
	try:
		u = float(u)
		v = float(v)
		a = float(a)
		return float((v**2 - u**2)/ (2 * a))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

#s=t(u+v)/2
def s_uvt(u:float, v:float, t:float) -> float:
	try:
		u = float(u)
		v = float(v)
		t = float(t)
		return float(((u + v)/ 2) * t)
	except ValueError:
		return "input error"

def u_svt(s:float, v:float, t:float) -> float:
	try:
		s = float(s)
		v = float(v)
		t = float(t)
		return float(((2 * s)/ t) - v)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def v_sut(s:float, u:float, t:float) -> float:
	try:
		s = float(s)
		u = float(u)
		t = float(t)
		return float(((2 * s)/ t) - u)
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

def t_suv(s:float, u:float, v:float) -> float:
	try:
		s = float(s)
		u = float(u)
		v = float(v)
		return float((2 * s)/ (u + v))
	except ValueError:
		return "input error"
	except ZeroDivisionError:
		return "Div/0"

