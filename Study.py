def is_palindromic():

	n = int(input("Enter the number: "))
	
	if( rev_num(n)== n):
		print("True")
	else:
		print("False")

	






def rev_num(n):
	rev_n=0
	while(n>0):
		rev_n =(rev_n*10)+(n%10)
		n=n//10
	return(rev_n)	



is_palindromic()	