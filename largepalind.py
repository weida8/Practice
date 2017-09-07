def isPal(n):
	if(int(str(n)[::-1]) == n):
		return True
	else:
		return False


def main():

	palinList = []
	for i in range(1000):

		for j in range(1000):

			if(isPal(i*j)):
				palinList.append(i*j)
	print(max(palinList))

main()


