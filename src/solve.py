# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-03T00:19:44+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-04T04:03:06+01:00

from src.error_handle import exit_error

def get_solution_nbr(list):
	discrim = (list[1] * list[1]) - (4 * list[0] * list[2])
	if (discrim == 0):
		return (1)
	elif (discrim > 0):
		return (2)
	return (0)

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

def solve_deg1(list):
	r = -list[0] / list[1]
	if (r % 1 == 0):
		r = int(r)
	return (str(r))

def solve_deg2(list, solution_nbr):
	if (list[2] == 0):
		exit_error(8)
	if (solution_nbr == 1):
		x = (list[1] * -1) / (2 * list[2])
		return (str(x))
	else:
		root = sq_root((list[1] * list[1]) - (4 * list[2] * list[0]))
		x = ((list[1] * -1) + root) / (2 * list[2])
		x_neg = ((list[1] * -1) - root) / (2 * list[2])
		return ("X = " + str(x) + ", X = " + str(x_neg))

def solve_eq(eq_degree, elem_list, sol_nbr):
	if (eq_degree == 0):
		if (elem_list[0] != 0):
			exit_error(7)
		else:
			print("\tAny real number is a solution for this equation" + "\n")
	elif (eq_degree == 1):
		print ("\t\033[93mThere is only one solution to this equation.\033[0m")
		print("\tThe answer is:")
		print("\tX = " + solve_deg1(elem_list) + "\n")
	else:
		print("\t\033[93mThis is a quadratic equation.\033[0m")
		print("\t\033[93mPossible real solutions: " + str(sol_nbr) + "\033[0m")
		if (sol_nbr == 0):
			print("\t\033[96mDiscriminant is strictly negative.\033[0m")
			print("\tCan't do, Bye!")
			exit(0)
		elif (sol_nbr == 1):
			print("\t\033[96mDiscriminant is zero (null)\033[0m.")
			print("\tSolution is:")
		else:
			print("\t\033[96mDiscriminant is strictly positive.\033[0m")
			print("\tSolutions are:")
		print("\t" + solve_deg2(elem_list, sol_nbr) + "\n")
