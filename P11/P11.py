import numpy as np

A=np.loadtxt('grid.txt')
B=np.transpose(A)

colrange=[4*k for k in range(5)]

max=0.0

for j in colrange: #compute rows
	for i in range(20):
		prod=A[i][j]*A[i][j+1]*A[i][j+2]*A[i][j+3]
		if prod > max:
			max=prod
		
rowmax=max

max=0.0
for j in colrange: #compute columns
	for i in range(20):
		prod=B[i][j]*B[i][j+1]*B[i][j+2]*B[i][j+3]
		if prod > max:
			max=prod

colmax=max

max=0.0
for j in range(17):  #compute diagonals
	for i in range(17):
		d1=A[i][j]*A[i+1][j+1]*A[i+2][j+2]*A[i+3][j+3]
		d2=A[i][j+3]*A[i+1][j+2]*A[i+2][j+1]*A[i+3][j]
		d=np.maximum(d1,d2)
		if d > max:
			max=d

diagmax=max

MAX=np.max([rowmax,colmax,diagmax])
print(MAX)
