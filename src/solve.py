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
	if (list[2] == 0):
		exit_error(8)
	if (solution_nbr == 1):
		x = (list[1] * -1) / (2 * list[2])
		return (str(x))
	else:
		root = sq_root((list[1] * list[1]) - (4 * list[2] * list[0]))
		x = ((list[1] * -1) + root) / (2 * list[2])
		x_neg = ((list[1] * -1) - root) / (2 * list[2])
		return (str(x) + ", " + str(x_neg))

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
