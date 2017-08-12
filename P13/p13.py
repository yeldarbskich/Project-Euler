import numpy as np

A=np.loadtxt('list.txt',dtype=str)
tot=(0,0,0,0,0,0,0,0,0,0,0,0,0)

for i in range(100):
	B=[k for k in A[i][2:15]]
#	if i==0:
#		print(B[0])
	tot=tot+np.array(B).astype(np.int64)

sum=0
for k in range(12):
	sum=sum+tot[k]*10**(5-k)

print(tot,sum)


