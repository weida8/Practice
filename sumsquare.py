def main():

	sumSquare =0
	totalSum =0
	for i in range(1,101):

		sumSquare += i**2

	for i in range(1, 101):

		totalSum += i 
	squareSum = totalSum**2



	answer = squareSum - sumSquare
	print(answer)

main()
