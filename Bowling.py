def main():
	gameList=[]
	inFile = open("score.txt","r")
	for game in inFile: #make each game in score.txt into a list 
		game = game.rstrip("\n")
		game=game.split()
		currentList=[]
		for score in game: #make a list of each game with x and / converted to int
			#print(score)
			if(score == "X"):
				currentList.append(10)
			elif(score == "-"):
				currentList.append(0)
			elif(score == "/"): #to let the game knows that it's a spare later on 
				currentList.append(11)
			else:
				currentList.append(int(score))
		currentScore=0
		currentScoreList=[]
		i=0
		frameCount=0
		print("currentgame frame:",currentList)
		while(i<len(currentList) and frameCount<=9): #add up the score and running score
			#print("currentscore:"+str(currentScore))
			#print("i:"+str(i))
			#print("frameCount:"+str(frameCount))
			if(frameCount<9):
				if(currentList[i] != 10 and currentList[i+1] != 11):
					currentScore+=currentList[i]+currentList[i+1]
					currentScoreList.append(currentScore)
					i+=2
				elif(currentList[i]==10 and currentList[i+2]==11):
					currentScore+=20
					currentScoreList.append(currentScore)
					i+=1
				elif(currentList[i]==10):
					currentScore+=(10+currentList[i+1]+currentList[i+2])
					currentScoreList.append(currentScore)
					i+=1
				elif(currentList[i+1]==11):
					currentScore+=10+currentList[i+2]
					currentScoreList.append(currentScore)
					i+=2
				frameCount+=1
			elif(frameCount==9):
				if(currentList[-4]==10 and currentList[-2]==11):
					currentScore+=10+currentList[-1]
					currentScoreList.append(currentScore)
				elif(currentList[i]==10 and currentList[i+2]==11):
					currentScore+=20
					currentScoreList.append(currentScore)
				elif(currentList[i]==10):
					currentScore+=10+currentList[i+1]+currentList[i+2]
					currentScoreList.append(currentScore)
				elif(currentList[i+1]==11):
					currentScore+=10+currentList[i+2]
					currentScoreList.append(currentScore)
				else:
					currentScore+=currentList[i]+currentList[i+1]
					currentScoreList.append(currentScore)
				frameCount+=1

		print("score list:", currentScoreList)



		#gameList.append(currentList)

	#print(gameList)
	inFile.close()
main()
