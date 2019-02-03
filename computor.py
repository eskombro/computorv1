import sys
from src.error_handle import test_errors, exit_error
from src.parse_params import balance_equation, get_balanced_str
from src.solve import get_solution_nbr, solve_deg1, solve_deg2, get_eq_degree

elem_list = []

s = test_errors(sys.argv)
elem_list = balance_equation(s)
print("Reduced form:       " + get_balanced_str(elem_list))
eq_degree = get_eq_degree(elem_list)
print("Polinomial degree:  " + str(eq_degree))
solution_nbr = get_solution_nbr(elem_list)

if (eq_degree == 0):
	if (elem_list[0] != 0):
		exit_error(7)
	else:
		print("Any real number is a solution for this equation")
elif (eq_degree == 1):
	print ("There is only one solution to this equation.\nThe anwer is:")
	print(solve_deg1(elem_list))
else:
	print("This is a quadratic equation.")
	print("Possible real solutions: " + str(solution_nbr))
	if (solution_nbr == 0):
		print("Discriminant is strictly negative.\nCan't do, Bye!")
		exit(0)
	elif (solution_nbr == 1):
		print("Discriminant is zero (null).\nSolution is:")
	else:
		print("Discriminant is strictly positive.\nSolutions are:")
	print(solve_deg2(elem_list, solution_nbr))
