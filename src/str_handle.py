def epur_str(s):
	i = 0
	while (i < len(s)):
		if (s[i] == ' '):
			if (i == 0 or i == len(s) - 1 or s[i + 1] == ' '):
				s = s[0 : i ] + s[i + 1 : len(s)]
				i -= 1
		i += 1
	return (s)

def check_wrong_chars(s):
	ok_chars = "+-*/=0123456789xX^ "
	for i in range(0, len(s)):
		if (ok_chars.find(s[i]) == -1):
			return (1)
	return (0)
