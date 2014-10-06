def factorial(x):
	if x==0:
		return 1
	else:
		return x*factorial(x-1)

print factorial(4)	

def Gamma(x):
	return factorial(x) + 5
print Gamma(4)
