# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-05T00:11:56+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-13T23:33:50+01:00

def is_num(c):
	if ("0123456789".find(c) == -1):
		return (0)
	return (1)

def handle_star(s, i):
	if (s[i + 1] != 'X'):
		s = s[0: i + 1] + "X^0" + s[i + 1: len(s)]
		if (i == 0 or not is_num(s[i - 1])):
			s = s[0: i] + "0" + s[i: len(s)]
		i = -1
	elif (i == 0 or (s[i - 1] != "." and not is_num(s[i - 1]))):
		s = s[0: i] + "1" + s[i: len(s)]
		i = -1
	elif (i == len(s) - 1 or s[i + 1] != 'X'):
		s = s[0: i] + s[i + 1: len(s)]
		i = -1
	return (s, i)

def handle_x(s, i):
	if (i < len(s) - 1 and is_num(s[i + 1])):
		s = s[0: i + 1] + "^" + s[i +1: len(s)]
		i = -1
	elif (i == 0 or s[i - 1] != '*'):
		if (i == 0 or is_num(s[i]) or s[i - 1] == '='):
			s = s[0: i] + "1*" + s[i: len(s)]
		else :
			s = s[0: i] + "*" + s[i: len(s)]
		i = -1
	elif (i == len(s) - 1 or s[i + 1] != '^'):
		s = s[0: i + 1] + "^1" + s[i + 1: len(s)]
		i = -1
	return (s, i)

def handle_num(s, i):
	prev = False
	next = False
	if (i == 0 or "+-=".find(s[i - 1]) != -1):
		prev = True
		while (i < len(s) - 1 and (is_num(s[i]) or s[i] == '.')):
			i += 1
		if (s[i - 1] == '.' and not is_num(s[i])):
			s = s[0: i] + "0" + s[i: len(s)]
			i = -1
		elif (i == len(s) or s[i] != '*'):
			if (i != len(s) - 1):
				i -= 1
			next = True
		if (s[i] == 'X' and i == len(s) - 1):
			s += "^1"
			i = -1
			prev = False
		if (prev and next):
			if (i == len(s) - 1 or "+-=".find(s[i + 1]) != -1):
				s = s[0: i + 1] + "*X^0" + s[i + 1: len(s)]
				i = -1
			elif (s[i + 1] == '.'):
				if(i < len(s) - 1 and not is_num(s[i + 2])):
					s = s[0: i + 2] + "0" + s[i + 2: len(s)]
					i = -1
	return (s, i)

def handle_point(s, i):
	if (i == 0 or not is_num(s[i - 1])):
		s = s[0: i] + "0" + s[i: len(s)]
		i = -1
	return (s, i)

def handle_human_format(s, verbose):
	i = 0
	print("\tFormat steps:") if verbose else 0
	while (i < len(s)):
		if (i == 0 and verbose):
			print("\t" + s)
		if (s[i] == '*'):
			s, i = handle_star(s, i)
		elif (s[i] == '.'):
			s, i= handle_point(s, i)
		elif (i < len(s) - 1 and s[i + 1] == 'X'):
			if (is_num(s[i])):
				s = s[0: i + 1] + "*" + s[i + 1: len(s)]
				i = -1
		elif (s[i] == 'X'):
			s, i = handle_x(s, i)
		elif (is_num(s[i])):
			s, i = handle_num(s, i)
		i += 1
	print("\n") if verbose else 0
	return (s)
