# @Author: Samuel Jimenez <sjimenez>
# @Date:\t2019-02-02T20:24:26+01:00
# @Email:  sjimenezre@gmail.com | sjimenez@student.42.fr
# @Last modified by:   sjimenez
# @Last modified time: 2019-02-05T23:32:14+01:00

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
	var = "\t\033[91m"
	if (erno != 0):
		var += "Error " + str(erno) + ": ("
	err_str = [	"Usage: python computor.py [ -v || -f ] arg",
				"Parameter 1 is not an equation)",
				"Equation format is wrong: several '=' symbols)",
				"Nothing before '=' symbol)",
				"Nothing after '=' symbol)",
				"Worng characters in the equation)",
				"This equation degree is a rational number)",
				"This equation is wrong! There's no solution!)",
				"Can't divide by zero! Sorry!)",
				"Parameter format is wrong)",
				"This equation degree is higher than 2 or smaller than 0)"]
	print(var + err_str[erno] + "\033[0m\n")
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
