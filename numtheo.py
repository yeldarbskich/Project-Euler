#Module for Number Theoretic computations
import numpy as np

def primes(n):
	"""Computes and returns the primes less than or equal to n. Inefficient for large n"""
	if n<5:
		if n==2:
			return [2]
		elif n==3:
			return [2,3]
		else:
			return [2,3]
	A=[k for k in range(n+1) if k>1]
	p=2
	primes=[2]
	while p <= n:
		if p > np.ceil(np.sqrt(n/2)):
			B=[p*x for x in A if p*x in A]
			A=[x for x in A if x not in B]
			A=A[1:]
			p=A[0]
			primes.append(A[0])
			break
		else:
			B=[p*x for x in A if p*x in A]
			A=[x for x in A if x not in B]
			A=A[1:]
			p=A[0]
			primes.append(A[0])

	primes=primes+(A[1:])
	return primes
	
def primefac(n):
	"""Computes the prime factorization of n. Output is a list of pairs (p,r) where p is the prime factor and r is the exponent. Optimized for numbers up to 40000. Dependencies: primes()."""
	if n==1:
		return 'cannot factor 1'
	if n <= 40000:
		P=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,169,173,179,181,191,193,197,199]
	else:
		P=primes(np.ceil(np.sqrt(n)))
	prod=1
	if n in P:
		return [(n,1)]
	else:
		primefac=[]
		tag=1
		for x in P:
			r=1
			if n % x == 0:
				if tag==1:
					tag=0
					if x > np.cbrt(n):
						if x != n//x:
							return [(x,1),(n//x,1)]
						else:
							return [(x,2)]
				while n % x**r == 0:
					r+=1
				prod = prod*(x**(r-1))
				primefac = primefac+[(x,r-1)]
				if prod == n:
					return primefac
		primefac=primefac+[(n//prod,1)]
		return primefac
			

def div(n,x):
	"""Computes the divisor function of n using primefac(n). x=0 gives the number of divisors, x=1 gives the sum of the divisors, x=k gives the sum of the k-powers of the divisors."""
	if n==1:
		return 1
	A=primefac(n)
	prod=1
	if x > 0:
		for y in A:
			prod = prod*(y[0]**((y[1]+1)*x)-1)//(y[0]**x-1)
	else:
		for y in A:
			prod = prod*(1+y[1])
	
	return prod

def div0(p,x):
	"""Input a prime factorization list of pairs [(p,r)] and outputs the divisor function for an integer parameter x. x=0 gives the number of divisors, x=1 gives the sum of the divisors, x=k gives the sum of the k-powers of the divisors."""
	prod=1
	if x > 0:
		for y in p:
			prod = prod*(y[0]**((y[1]+1)*x)-1)//(y[0]**x-1)
	else:
		for y in p:
			prod = prod*(1+y[1])
	
	return prod

def fac(n):
	"""Returns the value n! for postive integers n. Convention 0!=1"""
	if n==0:
		return 1
	return n*fac(n-1)

