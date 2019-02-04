# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-02T20:38:36+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-04T03:51:51+01:00

from src.error_handle import exit_error

def get_coef(par):
	chars = "0123456789."
	coef = 0
	degree = 0

	for i in range(0, len(par)):
		pos = chars.find(par[i])
		if (pos == -1):
			coef = float(par[0: i])
			tmp = par[par.find('^') + 1: len(par)]
			if (float(tmp) % 1 != 0 or int(tmp) > 2 or int(tmp) < 0):
				exit_error(6)
			degree = int(tmp)
			break
	return (coef, degree)

def handle_elems(s, is_left):
	elem_list = [0.0, 0.0, 0.0]

	while (len(s)):
		neg = 1
		if (s[0] == '-'):
			neg = -1
		s = s[1:len(s)]
		pos_sign = s.find('+')
		temp = s.find('-')
		if (temp != -1 and s[temp - 1] == '^'):
			temp = -1
		if (temp != -1 and (temp < pos_sign or pos_sign == -1)):
			pos_sign = temp
		if (pos_sign == -1):
			par = s
			s = ""
		else:
			par = s[0: pos_sign]
			s = s[pos_sign: len(s)]
		coef, degree = get_coef(par)
		if (not is_left):
			coef *= -1
		elem_list[degree] += coef * neg
	return (elem_list)

def balance_eq(s):
	elem_l = [0.0, 0.0, 0.0]
	elem_f = [0.0, 0.0, 0.0]

	eq_pos = s.find('=')
	s_l = s[0: eq_pos]
	s_r = s[eq_pos + 1: len(s)]
	if (s_l[0] != '-' and s_l[0] != '+'):
		s_l = "+" + s_l
	if (s_r[0] != '-' and s_r[0] != '+'):
		s_r = "+" + s_r
	elem_l = handle_elems(s_l, True)
	elem_r = handle_elems(s_r, False)
	for i in range(0,3):
		elem_l[i] += elem_r[i]
		elem_l[i] = round(elem_l[i], 4)
	return (elem_l)

def get_balanced_str(elem_list):
	str_balanced = ""
	for i in range(0, 3):
		if (elem_list[i]):
			if (i != 0 and elem_list[i] > 0.0 and elem_list[i - 1] != 0.0):
				str_balanced += "+ "
			if (elem_list[i] % 1 != 0):
				str_balanced += str(elem_list[i])
			else:
				str_balanced += str(int(elem_list[i]))
			str_balanced += "*X^" + str(i) + "  "
	if (str_balanced == ""):
		str_balanced += "0 "
	str_balanced += "=  0"
	return (str_balanced)

def handle_human_format(s):
	i = 0

	while (i < len(s)):
		if (s[i] == 'X'):
			if (i == 0 or s[i - 1] != '*'):
				s = s[0: i] + "1*" + s[i: len(s)]
				i = -1
			elif (i == len(s) - 1 or s[i + 1] != '^'):
				s = s[0: i + 1] + "^1" + s[i + 1: len(s)]
				i = -1
		elif ("0123456789".find(s[i]) != -1):
			prev = False
			next = False
			if (i == 0 or "+-=".find(s[i - 1]) != -1):
				prev = True
				while (i < len(s) - 1 and "0123456789.".find(s[i]) != -1):
					i += 1
				if (i == len(s) or s[i] != '*'):
					if (i != len(s) - 1):
						i -= 1
					next = True
				if (prev and next):
					s = s[0: i + 1] + "*X^0" + s[i + 1: len(s)]
					i = -1
		i += 1
	return (s)
