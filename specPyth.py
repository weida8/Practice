def main():

	answer = 1000
	for i in range(1, answer//2):
		for j in range(1, answer//2):
			for k in range(1, answer//2):
				if(i**2 + j**2 == k**2 and i+j+k == answer):
					print(i*j*k)

main()