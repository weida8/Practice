def isPrime(n):

	for i in range(2, n):
		if(n%i == 0):
			return False
	return(True)

def main():

	number = 1
	count = 0
	while(count<=6):
		if(isPrime(number)):
			count += 1
		number += 1
	print(number)

main()