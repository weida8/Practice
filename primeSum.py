def isPrime(n):

	for i in range(2, n):
		if(n%i == 0):
			return False
	return True

def main():

	totalSum =0
	for i in range(2, 2000000):
		if(isPrime(i)):
			print(i)
			totalSum += i

	print(totalSum)

main()
