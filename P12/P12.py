import numpy as np
import numtheo2 as nt

max=1
#r=np.sqrt(500)
for n in range(20000)[9999:]:
	if n % 2 == 0:
		p=nt.div(n//2,0)*nt.div(n+1,0)
	else:
		p=nt.div(n,0)*nt.div((n+1)//2,0)
	if p>max:
		max=p
		thing=(n,n*(n+1)//2)
	if max >= 500:
		break

print(max,thing)
