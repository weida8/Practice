#  File: Books.py

#  Description: Assignment 13

#  Student Name: Wei-Da Pan

#  Student UT EID: wp3479

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 5/4/15

#  Date Last Modified: 5/6/15
def main():
	# Create word dictionary from comprehensive word list
	comp_dict=create_word_dict()
	word_dict1={}
	word_dict2={}
	# Enter names of the two books in electronic form
	book1 = str(input ("Enter name of first book: "))
	book2 = str(input ("Enter name of second book: "))
	print("")
	book1text=open(book1,"r")
	book2text=open(book2,"r")

	dict1=getWordFreq(book1text)
	dict2=getWordFreq(book2text)

	#create a list of words with just capitalized words
	capped_words=[]
	key=dict1.keys()
	for words in key:
  		low_words=words.lower()
  		if(words != low_words):
  			capped_words.append(words)

  	#check with book1 and dictionary to see if the word is a pronoun and add or delete 
	for words in capped_words:
  		low_words=words.lower()
  		if low_words in dict1:
  			dict1[low_words] +=1
  			del dict1[words]
  		elif low_words in comp_dict:
  			dict1[low_words] =1
  			del dict1[words]
  		else:
  			del dict1[words]
	
	#create a list of words with just capitalized words
	capped_words=[]
	key2=dict2.keys()
	for words in key2:
  		low_words=words.lower()
  		if(words != low_words):
  			capped_words.append(words)

  	#check with book2 and dictionary to see if the word is a pronoun and add or delete
	for words in capped_words:
  		low_words=words.lower()
  		if low_words in dict2:
  			dict2[low_words] +=1
  			del dict2[words]
  		elif low_words in comp_dict:
  			dict2[low_words] =1
  			del dict2[words]
  		else:
  			del dict2[words]

	book1text.close()
	book2text.close()

  # Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ") 
	print("")
 
	#print output for first author
	distinct_words=len(dict1)
	total_words=sum(int(x) for x in dict1.values())
	print(author1)
	print("Total distinct words = ", distinct_words)
	print("Total words (including duplicates) = ", total_words)
	print("Ratio(%  of total distinct words to total words) = " ,(distinct_words/total_words)*100, "\n")


	#print output for second author
	distinct_words2=len(dict2)
	total_words2=sum(int(x) for x in dict2.values())
	print(author2)
	print("Total distinct words = ", distinct_words2)
	print("Total words (including duplicates) = ", total_words2)
	print("Ratio(%  of total distinct words to total words) = " ,(distinct_words2/total_words2)*100, "\n")
	unique_word_list1=[]
	unique_word_list2=[]

	for words in key:
		unique_word_list1.append(words)
	for words in key2:
		unique_word_list2.append(words)

	#find words not used by the other author
	author1_unique_words=len(set(unique_word_list1) - set(unique_word_list2))
	author2_unique_words=len(set(unique_word_list2) - set(unique_word_list1))

	unique_set1=set(unique_word_list1) - set(unique_word_list2)
	unique_set2=set(unique_word_list2) - set(unique_word_list1)

	#calculate the frequency of the words that's unique
	unique_freq=0
	unique_freq2=0
	for words in unique_set1:
		unique_freq += dict1[words]
	for words in unique_set2:
		unique_freq2 += dict2[words]
	relative_freq1=(unique_freq/total_words)*100
	relative_freq2=(unique_freq2/total_words2)*100

	print(author1, "used", author1_unique_words,"words that", author2, "did not use.")
	print("Relative frequency of words used by",author1, "not in common with", author2,"=", relative_freq1,"\n")

	print(author2, "used", author2_unique_words,"words that", author1, "did not use.")
	print("Relative frequency of words used by",author2, "not in common with", author1,"=", relative_freq2)
	


# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
	dictionary=open("words.txt","r")
	for line in dictionary:
		line=line.strip()
		word_list=line.split()
		for word in word_list:
			if word in word_dict:
				word_dict[word] +=1
			else:
				word_dict[word] = 1 
	return(word_dict)	
	dictionary.close()

# Removes punctuation marks from a string
def parseString (st):
	s=" "
	s2=" "
	for ch in st:
		if(ch>="a" and ch<"z" or ch>="A" and ch<="Z"):
			s+=ch
		else:
			s+=" "
	if "'s" in s:
		s.replace("'s"," ")
	if(s[-1]=="'"):
		s[:-1]
	return s

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
	word_dict={}
	for line in file:
  		line=line.strip()
  		line=parseString(line)
	  	word_list=line.split()
	  	for word in word_list:
	  		if word in word_dict:
	  			word_dict[word] +=1
	  		else:
	  			word_dict[word]=1
	return(word_dict)



main()
