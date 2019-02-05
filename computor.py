# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-02T20:24:15+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-05T19:22:59+01:00

import sys

from src.header import print_header
from src.error_handle import test_errors, exit_error
from src.human_format import handle_human_format
from src.parse_params import balance_eq, get_balanced_str
from src.solve import get_solution_nbr, get_eq_degree, solve_eq

verbose = 0
elem_list = []
args = sys.argv

if (len(args) > 3):
	exit_error(0)
if (len(args) == 3):
	if (args[1] != "-v"):
		exit_error(0)
	verbose = 1
	args = [args[0], args[2]]

print_header()
s = test_errors(args)
s = handle_human_format(s, verbose)
elem_list = balance_eq(s)
print("\t\033[92mReduced form:\033[0m       " + get_balanced_str(elem_list))
eq_degree = get_eq_degree(elem_list)
print("\t\033[92mPolinomial degree:\033[0m  " + str(eq_degree))
solution_nbr, discrim = get_solution_nbr(elem_list)
solve_eq(eq_degree, elem_list, solution_nbr, discrim)
