import numtoeng as eng

sum=0
for k in [i for i in range(1000) if i >0]:
	if k<101:
		print(eng.numtoeng(k))
	sum=len(eng.numtoeng(k))+sum

print(sum+len('onethousand'))
