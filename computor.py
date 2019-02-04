# @Author: Samuel Jimenez <sjimenez>
# @Date:   2019-02-02T20:24:15+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-04T03:46:43+01:00

import sys

from src.header import print_header
from src.error_handle import test_errors
from src.parse_params import balance_eq, get_balanced_str, handle_human_format
from src.solve import get_solution_nbr, get_eq_degree, solve_eq

elem_list = []

print_header()
s = test_errors(sys.argv)
s = handle_human_format(s)
elem_list = balance_eq(s)
print("\t\033[92mReduced form:\033[0m       " + get_balanced_str(elem_list))
eq_degree = get_eq_degree(elem_list)
print("\t\033[92mPolinomial degree:\033[0m  " + str(eq_degree))
solution_nbr = get_solution_nbr(elem_list)
solve_eq(eq_degree, elem_list, solution_nbr)
