def divlist(n):
	finaldivList = []
	for i in range(1, n+1):
		if(n%i == 0):
			finaldivList.append(i)
	return finaldivList

def main():

	divNum = 0
	triNum = 1
	triCount = 1
	while(divNum <= 500):
		for naturalnumber in range(1,triCount+1):
			triNum += naturalnumber
		divNum = len(divlist(triNum))
	print(triNum)

main()



