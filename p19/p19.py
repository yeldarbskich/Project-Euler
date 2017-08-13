def myrange(n):
	return [k for k in range(n+1) if k>0]

year=myrange(31)+myrange(28)+myrange(31)+myrange(30)+myrange(31)+myrange(30)+myrange(31)+myrange(31)+myrange(30)+myrange(31)+myrange(30)+myrange(31)
leap=myrange(31)+myrange(29)+myrange(31)+myrange(30)+myrange(31)+myrange(30)+myrange(31)+myrange(31)+myrange(30)+myrange(31)+myrange(30)+myrange(31)

#print(year[6])
#print(leap)

x=6
tot=0

for k in range(2001)[1901:]:
	if k % 4 == 0 & k % 400 != 0:
		p=0
		while x+7*p <= len(leap)-1:
			if leap[x+7*p] == 1:
				tot+= 1
			p+=1
		x=((x+7*p) % len(leap))-1
	else:
		p=0
		while x+7*p <= len(year)-1:
			if year[x+7*p] == 1:
				tot+= 1
			p+=1
		x=((x+7*p) % len(year))-1

print(tot)
