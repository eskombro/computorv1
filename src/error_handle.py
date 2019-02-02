from src.str_handle import epur_str, check_wrong_chars

def exit_error(erno):
	print("Error:")
	err_str = [	"Worng number of parameters. Expected 1.",
				"Parameter 1 is not an equation",
				"Equation format is wrong: several '=' symbols",
				"Nothing before '=' symbol",
				"Nothing after '=' symbol",
				"Worng characters in the equation"]
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
