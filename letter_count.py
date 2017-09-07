def main():
	total = 0
	final = 1001
	and_word = 3
	one_nine = 45
	ten_teen = 80
	twenty_ninety = 54
	hundred = 7
	thousand = 8
	for count in range(1, final):
		if(count==10):
			total += one_nine
			print(total)
		elif(count == 99):
			ty_total  = ten_teen+twenty_ninety+(80*one_nine)
			total += ty_total
			print(total)
		elif(count == 1000):
			total += (one_nine)+(9*hundred)+(729*and_word)+(9*ty_total)+(90*one_nine)+3+thousand
	print(total)
	
main()		 