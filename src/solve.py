# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-03T00:19:44+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-13T23:33:18+01:00

from src.error_handle import exit_error
from decimal import *

def get_solution_nbr(list):
	discrim = (list[1] * list[1]) - (4 * list[0] * list[2])
	if (discrim == 0):
		return (1, discrim)
	elif (discrim > 0):
		return (2, discrim)
	else:
		return (2, discrim)

def get_eq_degree(list):
	eq_degree = 0
	for i in range(1,3):
		if (list[i] != 0):
			eq_degree = i
	return(eq_degree)

def sq_root(nbr):
	x = 0.0
	increm = nbr / 100
	i = 0

	while (x * x < nbr):
		x += increm
		if (x * x > nbr):
			x-=increm
			increm /= 2
		i += 1
		if (i == 300):
			break
	return (x)

def convert_fraction(s, fractions):
	found = False
	getcontext().prec = 12
	nbr = 0 if (Decimal(s) == -0.0) else Decimal(s)
	s = str(nbr)
	if (fractions):
		res = ""
		nbr = Decimal(s)
		if (nbr < 0.0):
			res += "-"
			nbr *= -1
		if (nbr % 1 == 0):
			return (s)
		natural = int(nbr)
		decimal = Decimal(nbr - natural)
		nom = Decimal(1.0)
		den = Decimal(1.0)
		while (not found and nom <= 100):
			while (not found and den <= 100):
				calc = Decimal(str(nom/den))
				if (calc == decimal):
					found = True
					if (natural != 0):
						res += str(natural)
					res += "(" + str(int(nom)) + "/" + str(int(den)) + ")"
					break
				den += Decimal(1.0)
				if (calc < decimal):
					den = Decimal(101)
			den = Decimal(1.0)
			nom += Decimal(1.0)
	if (not found):
		return (s)
	return (res)

def solve_deg1(list, fractions):
	r = -list[0] / list[1]
	if (r % 1 == 0):
		r = int(r)
	return (convert_fraction(str(r), fractions))

def solve_deg2(list, solution_nbr, discrim, fractions):
	if (list[2] == 0):
		exit_error(8)
	if (solution_nbr == 1):
		x = (list[1] * -1) / (2 * list[2])
		return (convert_fraction(str(x), fractions))
	elif (discrim > 0):
		root = sq_root((list[1] * list[1]) - (4 * list[2] * list[0]))
		x = ((list[1] * -1) + root) / (2 * list[2])
		str_x = convert_fraction(str(x), fractions)
		x_neg = ((list[1] * -1) - root) / (2 * list[2])
		str_x_neg = convert_fraction(str(x_neg), fractions)
		return ("X = " + str_x + ", X = " + str_x_neg)
	else:
		root = sq_root(-1 * discrim)/ (2 * list[2])
		if (root < 0):
			root *= -1
		x = ((list[1] * -1)) / (2 * list[2])
		str_x = convert_fraction(str(x), fractions) + " + "
		str_x += convert_fraction(str(root), fractions) + " i"
		str_x_neg = convert_fraction(str(x), fractions) + " - "
		str_x_neg += convert_fraction(str(root), fractions) + " i"
		return ("X = " + str_x + ", X = " + str_x_neg)

def solve_eq(eq_degree, elem_list, sol_nbr, discrim, fractions):
	if (eq_degree == 0):
		if (elem_list[0] != 0):
			exit_error(7)
		else:
			print("\tAny real number is a solution for this equation" + "\n")
	elif (eq_degree == 1):
		print ("\t\033[93mThere is only one solution to this equation.\033[0m")
		print("\tThe answer is:")
		print("\tX = " + solve_deg1(elem_list, fractions) + "\n")
	else:
		print("\t\033[93mThis is a quadratic equation.\033[0m")
		print("\t\033[93mPossible solutions: " + str(sol_nbr) + "\033[0m")
		if (sol_nbr == 1):
			print("\t\033[96mDiscriminant is zero (null)\033[0m.")
			print("\tSolution is:")
			print("\t" + solve_deg2(elem_list, sol_nbr, discrim, fractions) + "\n")
		elif (discrim > 0):
			print("\t\033[96mDiscriminant is strictly positive.\033[0m")
			print("\tSolutions are:")
			print("\t" + solve_deg2(elem_list, sol_nbr, discrim, fractions) + "\n")
		else:
			print("\t\033[96mDiscriminant is strictly negtive.\033[0m")
			print("\tSolutions are:")
			print("\t" + solve_deg2(elem_list, sol_nbr, discrim, fractions) + "\n")
