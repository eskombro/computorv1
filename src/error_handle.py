# @Author: Samuel Jimenez <sjimenez>
# @Date:\t2019-02-02T20:24:26+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-04T03:49:00+01:00

def epur_str(s):
	i = 0
	while (i < len(s)):
		if (s[i] == ' '):
			s = s[0 : i ] + s[i + 1 : len(s)]
			i -= 1
		i += 1
	return (s)

def check_wrong_chars(s):
	ok_chars = "X+-*/=0123456789^. "
	for i in range(0, len(s)):
		if (ok_chars.find(s[i]) == -1):
			return (1)
	return (0)

def exit_error(erno):
	print("\tError: " + str(erno))
	err_str = [	"\tWorng number of parameters. Expected 1.",
				"\tParameter 1 is not an equation",
				"\tEquation format is wrong: several '=' symbols",
				"\tNothing before '=' symbol",
				"\tNothing after '=' symbol",
				"\tWorng characters in the equation",
				"\tThis equation degree is different than 0, 1 or 2",
				"\tThis equation is wrong! There's no solution!",
				"\tCan't divide by zero! Sorry!"]
	print(err_str[erno])
	exit (1)

def test_errors(argv):
	if (len(argv) != 2):
		exit_error(0)
	eq_str = epur_str(str(argv[1]))
	eq_pos = eq_str.find("=")
	if (eq_pos == -1):
		exit_error(1)
	if (eq_str[eq_pos + 1:len(eq_str)].find("=") != -1):
		exit_error(2)
	if (not len(eq_str[0:eq_pos])):
		exit_error(3)
	if (not len(eq_str[eq_pos + 1:len(eq_str)])):
		exit_error(4)
	if (check_wrong_chars(eq_str)):
		exit_error(5)
	return (eq_str)
