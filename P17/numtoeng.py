def numtoeng(n):
	"""Takes a positive integer n and outputs the string of english words corresponding to that number"""
	X=str(n)
	k=len(X)
	eng=''
	for i in range(k):
		if i % 3 == 0:
			if int(X[-2:])<=10 or int(X[-2:])>=20:
				eng=ten(int(X[-1]))+eng
		elif i % 3 == 1:
			if 10<int(X[-2:])<20:
				eng=teen(int(X[-1]))+eng
			else:
				eng=ifty(int(X[-2]))+eng
		else:
			if n % 100 == 0:
				eng=ten(int(X[-3]))+'hundred'+eng
			else:
				eng=ten(int(X[-3]))+'hundredand'+eng
	return eng

def ten(n):
	"""Takes a number n between 0 and 9 and returns the english"""
	if n>9:
		return 'you broke ten'
	else:
		if n == 1:
			return 'one'
		if n == 2:
			return 'two'
		if n == 3:
			return 'three'
		
		if n == 4:
			return 'four'
		
		if n == 5:
			return 'five'
		
		if n == 6:
			return 'six'
		
		if n == 7:
			return 'seven'
		
		if n == 8:
			return 'eight'
		if n == 9:
			return 'nine'
		if n== 0:
			return ''

def ifty(n):
	"""Takes a number n between 0 and 9 and returns the english tens version"""
	if n>9:
		return 'you broke ifty'
	else:
		if n == 1:
			return 'ten'
		if n == 2:
			return 'twenty'
		if n == 3:
			return 'thirty'
		
		if n == 4:
			return 'forty'
		
		if n == 5:
			return 'fifty'
		
		if n == 6:
			return 'sixty'
		
		if n == 7:
			return 'seventy'
		
		if n == 8:
			return 'eighty'
		if n == 9:
			return 'ninety'
		if n== 0:
			return ''

def teen(n):
	"""Takes a number n between 0 and 9 and returns the english teens version"""
	if n>9:
		return 'you broke teen'
	else:
		if n == 1:
			return 'eleven'
		if n == 2:
			return 'twelve'
		if n == 3:
			return 'thirteen'
		
		if n == 4:
			return 'fourteen'
		
		if n == 5:
			return 'fifteen'
		
		if n == 6:
			return 'sixteen'
		
		if n == 7:
			return 'seventeen'
		
		if n == 8:
			return 'eighteen'
		if n == 9:
			return 'nineteen'
		if n== 0:
			return ''



