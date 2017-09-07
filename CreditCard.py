def main():

	cardnumber = int(input("Enter 15 or 16-digit credit card number: "))
	numberlength = len(str(cardnumber))
	if(numberlength==15 or numberlength==16):
		if(is_valid(cardnumber)==1):
			print("Valid", cc_type(cardnumber))
		else:
			print("Invalid credit card number")
	else:
		print("Not a 15 or 16-digit number")
		return	

def is_valid(n):
	totalsum=0
	while(n>0):
		oddtotal =0
		regularodd=0
		eventotal=0
		y=0
		x = (n%10)
		y =2*x
		if(x%2==1 and y>=10):
			oddtotal = oddtotal + (2*x%10) + (2*x//10)
		elif(x%2==1):
			regularodd = regularodd+(2*x)
		else:
			eventotal = eventotal+x
		n=n//10	

		totalsum = totalsum+oddtotal+regularodd+eventotal
	if(totalsum%10==0):
		return(1)	
	else:
		return(0)

def cc_type(n):
	i = len(str(n))
	while(i>0):
		x = n//10
		i=i-1
		if(i==4 and x==6011 or i==3 and x==644 or i==2 and x==65):
			return("Discover Card number")
		if(i==2 and x==34 or x==37):
			return("American Express Card number")
		if(i==2 and x==50 or x==51 or x==52 or x==53 or x==54 or x==55):
			return("MasterCard number")
		if(i==1 and x==4):
			return("Visa Card number")
		n=n//10		
		
main()


			
