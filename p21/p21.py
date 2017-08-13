import numtheo2 as nt

def s(n):
	"""Returns the sum of the proper divisors of n"""
	return nt.div(n,1)-n

sum=0
for a in [k for k in range(10000) if k >0]:
	b=s(a)
	if b<10000:
		if a==s(b) and a<b:
			print(a,b)
			sum=sum+a+b

print(sum)
