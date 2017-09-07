#  File: playpoker.py
#  Description: homework assignment 3 play poker
#  Student's Name: Wei-Da Pan
#  Student's UT EID: Wei-Da Pan
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 9/23/15
#  Date Last Modified: 9/26/15

#I've had a really rough week and didn't get a chance to really work on this until friday night
#I understand that my program doesn't run properly but I don't think I can fix it before 2 days late


# import the random number generator
# this is needed to shuffle the cards into a random order

import random

class Card (object):
  RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

  SUITS = ['C', 'D', 'H', 'S']

  def __init__ (self, rank, suit):
    # each Card object consists of two attributes: a rank
    #    and a suit
    self.rank = rank
    self.suit = suit
    
  def __str__ (self):
    # print J, Q, K, A instead of 11, 12, 13, 14
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # you'll find the following methods to be useful:  they 
  #    allow you to compare Card objects

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)


class Deck (object):

  def __init__ (self):
    # self.deck is the actual deck of cards
    # create it by looping through all SUITS and RANKS
    #    and appending them to a list
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append(card)


  def shuffle (self):
    # the shuffle method in the random package reorders
    #    the contents of a list into random order
    random.shuffle (self.deck)

  def deal (self):
    # if the deck is empty, fail:  otherwise pop one
    #    card off and return it
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)

  def __str__(self):
    for card in self.deck:
      print(str(card))
      
class Poker (object):
  #
  # when you create an object of class Poker, you
  #    create a deck, shuffle it, and deal cards
  #    out to the players.
  #
  def __init__ (self, numHands):
    self.deck = Deck()              # create a deck
    self.deck.shuffle()             # shuffle it
    self.hands = []
    numCards_in_Hand = 5

    for i in range (numHands):
      # deal out 5-card hands to numHands players
      # you'd actually get shot if you dealt this
      #    way in a real poker game (5 cards to
      #    the first player, 5 to the next, etc.)
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  def play (self):
    sortedHands = []
    for i in range (len(self.hands)):
      # the method "sorted" returns a sorted list without
      #   altering the original list.  reverse = True
      #   makes it sort in decreasing order
      sortedHand = sorted (self.hands[i], reverse = True)
      sortedHands.append(sortedHand)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)

      #creates a list named handscore and call all the methods that will fill up 
      #the score value for each hand
      handscore=[]
      is_royal(sortedHands, handscore)
      is_straight_flush(sortedHands, handscore)
      is_four(sortedHands, handscore)
      is_full(sortedHands, handscore)
      is_flush(sortedHands, handscore)
      is_straight(sortedHands, handscore)
      is_three(sortedHands, handscore)
      is_two(sortedHands, handscore)
      is_one(sortedHands, handscore)
      is_high(sortedHands, handscore)

      #prints out what each hands are
      for score in handscore:
        i = 1
        if(score == 10):
          print("Hand " + i + ": Royal Flush")
        elif(score == 9):
          print("Hand " + i + ": Straight Flush")
        elif(score == 8):
          print("Hand " + i + ": Four of a Kind")
        elif(score == 7):
          print("Hand " + i + ": Full House")
        elif(score == 6):
          print("Hand " + i + ": Flush")
        elif(score == 5):
          print("Hand " + i + ": Straight")
        elif(score == 4):
          print("Hand " + i + ": Three of a Kind")
        elif(score == 3):
          print("Hand " + i + ": Two Pair")
        elif(score == 2):
          print("Hand " + i + ": One Pair")
        else:
          print("Hand " + i + ": High Card")

        #prints out who the winner is 

        if(i<2):
          highscore = score
          highscoreplace = i
        else:
          if(highscore<score):
            highscore = score
            highscoreplace = i 
          elif(highscore == score):
            total_points1 = highscore * 13**5 + sortedHands[i-2][0] * 13**4 + sortedHands[i-2][1] * 13**3 + sortedHands[i-2][2] * 13**2 + sortedHands[i-2][3] * 13 + sortedHands[i-2][4]
            total_points2 = score * 13**5 + sortedHands[i-1][0] * 13**4 + sortedHands[i-1][1] * 13**3 + sortedHands[i-1][2] * 13**2 + sortedHands[i-1][3] * 13 + sortedHands[i-1][4]
            if(total_points1>total_points2):
              print("Hand " + i-1 + " wins.")
              break
            else:
              print("Hand " + i + " wins.")
              break
          i += 1
        print("Hand " + i + " wins.")

      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5

    def is_royal (self, sortedHands, handscore):
    #uses sortedhands to check cards
    #check each cards for their rank and suit
    #if first card's rank is not 10 then return 0 
    #if any card suit isnt the same as the previous then return 0 
      handnumber = 0
      for hand in sortedHands:
        if(handscore[handnumber]!=0):
          continue
        else:
          for card in hand:
            cardnumber = 0
            if(card.rank != 14):
              handscore[handnumber] = 0
              break
            else:
              if(cardnumber==1):
                prevsuit = card.suit
                prevrank = card.rank
              else:
                if(prevsuit!=card.suit or prevrank-1 != card.rank):
                  handscore[handnumber] = 0
                  break
                else:
                  continue
            cardnumber+=1
          handscore[handnumber]=10
          handnumber+=1
      return(handscore) 

  def is_straight_flush (self, sortedHands, handscore):

    #run through each hand and each card and check to see
    #if the previous rank is the same as the current one
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        for card in hand:
          cardnumber = 0
          if(cardnumber==1):
            prevsuit = card.suit
            prevrank = card.rank
          else:
            if(prevsuit!=card.suit or prevrank-1 != card.rank):
              handscore[handnumber] = 0
              break
            else:
              continue
        cardnumber+=1
        handscore[handnumber]=9
        handnumber+=1
    return(handscore)

  def is_four (self, sortedHands, handscore):

    #loop through each hand and card and check to see previous rank is the same as 
    #current just for four cards
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        for card in hand:
          cardnumber = 0
          if(cardnumber==1):
            prevrank = card.rank
          else:
            if(cardnumber==2 and prevrank != card.rank):
              handscore[handnumber] = 0
              break
            elif(cardnumber>2 and prevrank != card.rank):
              handscore[handnumber] = 0
            else:
              continue
          cardnumber+=1
        handscore[handnumber]=8
        handnumber+=1
    return(handscore)

  def is_full (self, sortedHands, handscore):
    #calling each rank of the card in each hand to check to see if they are equal
    #to each other 
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].rank==hand[1].rank and (hand[2].rank==hand[3].rank and hand[3].rank==hand[4].rank) and hand[0].rank!=hand[5].rank):
          handscore[handnumber] = 7
        elif((hand[0].rank==hand[1].rank and hand[1].rank==hand[2].rank) and hand[3].rank==hand[5].rank and hand[0].rank!=hand[5].rank):
          handscore[handnumber] = 7
        else:
          handscore[handnumber] = 0 
        handnumber += 1
    return(handscore)

  def is_flush (self, sortedHands, handscore):

    #calling each suit of the card in each hand to see if they are all the same
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].suit == hand[1] and hand[0].suit == hand[2] and hand[0].suit == hand[3] and hand[0].suit == hand[4]):
          handscore[handnumber] = 6
        else:
          handscore[handnumber] = 0
        handnumber += 1
    return(handscore)

  def is_straight (self, sortedHands, handscore):

    #calling each rank of the card and check to see
    #if the previous card is one higher than current
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].rank-1 == hand[1].rank and hand[1].rank-1 == hand[2] and hand[2].rank-1 == hand[3] and hand[3].rank-1 == hand[4]):
          handscore[handnumber] = 5
        else:
          handscore[handnumber] = 0
        handnumber += 1
    return(handscore)

  def is_three (self, sortedHands, handscore):

    #calling each card rank to check all the combinations of three of a kind
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank):
          handscore[handnumber] = 4
        elif(hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank):
          handscore[handscore] = 4
        elif(hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank):
          handscore[handnumber] = 4
        else:
          handscore[handnumber] = 0
        handnumber += 1
    return(handscore)

  def is_two (self, sortedHands, handscore):

    #calling each card rank to check all the combinations of two pair
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank):
          handscore[handnumber] = 3
        elif(hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank):
          handscore[handnumber] = 3
        elif(hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
          handscore[handnumber] = 3
        else:
          handscore[handnumber] = 0
    return(handscore)

  def is_one (self, sortedHands, handscore):
    #calling each card rank to check all the combinations of one pair
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand[0].rank==hand[1].rank):
          handscore[handnumber] = 2
        elif(hand[1].rank == hand[2].rank):
          handscore[handnumber] = 2
        elif(hand[2].rank == hand[3].rank):
          handscore[handnumber] = 2
        elif(hand[3].rank == hand[4].rank):
          handscore[handnumber] = 2
        else:
          handscore[handnumber] = 0
    return(handscore)  

  def is_high (self, sortedHands, handscore):
    #if it's not either of the above methods set handscore to 1
    handnumber = 0
    for hand in sortedHands:
      if(handscore[handnumber]!=0):
        continue
      else:
        if(hand!=is_royal and hand!=is_straight_flush and hand!=is_straight and hand!=is_four and hand!=is_full and hand!=is_flush and hand!=is_straight and hand!=is_three and hand!=is_two and hand!=is_one):
          handscore[handnumber] = 1
        handnumber += 1
    return(handscore)

def main():

  print(str(Deck()))
  numHands = int (input ('Enter number of hands to play: '))

  # need at least 2 players but no more than 6
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))

  # create a Poker object:  create a deck, shuffle it, and
  # deal out the cards
  game = Poker (numHands)

  # play the game
  game.play()

main()
