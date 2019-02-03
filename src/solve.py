def get_solution_nbr(list):
	discrim = (list[1] * list[1]) - (4 * list[0] * list[2])
	if (discrim == 0):
		return (1)
	elif (discrim > 0):
		return (2)
	return (0)

def solve_deg1(list):
	r = -list[0] / list[1]
	if (r % 1 == 0):
		r = int(r)
	return (str(r))

def solve_deg2(list, solution_nbr):
	if (solution_nbr == 1):
		return ("Some solution")
	else:
		return ("Some solution, and some other")

def get_eq_degree(list):
	eq_degree = 0
	for i in range(1,3):
		if (list[i] != 0):
			eq_degree = i
	return(eq_degree)
