def fact(n):
	if(n<2):
		return n
	else:
		return n*fact(n-1)

def factSum(n):
	if(len(str(n))<2):
		return n
	else:
		return n%10+factSum(n//10)

def main():

	print(factSum(fact(100)))

main()