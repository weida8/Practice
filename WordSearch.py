def main():
	import string 
	in_file=open("hidden.txt","r")
	out_file=open("found.txt","w")
	line=in_file.readline()
	line=line.strip()
	line=line.split()
	m=int(line[0])
	n=int(line[1])
	line=in_file.readline()

	matrix=[]
	for i in range(m):
		n_list=[]
		line=in_file.readline()
		line=line.strip()
		n_list=line.split()
		matrix.append(n_list)
	line=in_file.readline()

	line=in_file.readline()
	line=line.strip()

	dict_num=int(line)
	Wordlist=[]
	for i in range(dict_num):
		line=in_file.readline()
		line=line.strip()
		word=line.split()
		Wordlist.append(word)

	tran_matrix=[]
	for j in range(len(matrix[0])):
		new_row=[]
		for i in range(len(matrix)):
			new_row.append(matrix[i][j])
		tran_matrix.append(new_row)

	
	output_string=""
	for i in Wordlist:
		wordfound=False
		current_word="".join(i)
		row_number=0
		for j in matrix:
			list_string=""
			row_number+=1
			for k in j:
				list_string=list_string+k
				string_rev=list_string[::-1]
			if(current_word in list_string):
				wordfound=True		
				word_idx=(list_string.rfind(current_word))+1
				if(wordfound):
					output_string=output_string+current_word+", "+str(row_number)+", "+str(word_idx)+"\n"
			elif(current_word in string_rev):
				wordfound=True
				rev_word_idx=(string_rev.rfind(current_word))
				word_idx=m-(rev_word_idx+1)+1
				if(wordfound):
					output_string=output_string+current_word+", "+str(row_number)+", "+str(word_idx)+"\n"

		row_number=0			
		for j in tran_matrix:
			list_string=""
			row_number+=1
			for k in j:
				list_string=list_string+k
			if(current_word in list_string or current_word in list_string[::-1]):
				wordfound=True		
				word_idx=(list_string.rfind(current_word))+1
				if(wordfound):
					output_string=output_string+current_word+", "+str(word_idx)+", "+str(row_number)+"\n"
			elif(current_word in string_rev):
				wordfound=True
				rev_word_idx=(string_rev.rfind(current_word))
				word_idx=m-(rev_word_idx+1)+1
				if(wordfound):
					output_string=output_string+current_word+", "+str(word_idx)+", "+str(row_number)+"\n"
		if(wordfound==False):
			output_string=output_string+current_word+", "+"0"+", "+"0"+"\n"

	out_file.write(output_string)
main()