import sys
from src.error_handle import test_errors
from src.parse_params import balance_equation, get_balanced_str


elem_list = []
verbose = 1

s = test_errors(sys.argv)
if (verbose):
	print("Clean equation:    |" + s + "|")

elem_list = balance_equation(s)
if (verbose):
	print("Clean equation:    |" + get_balanced_str(elem_list) + "|")

eq_degree = 0
for i in range(1,3):
	if (elem_list[i] != 0):
		eq_degree += 1
print("Polinomial degree:     | " + str(eq_degree) + " |")
