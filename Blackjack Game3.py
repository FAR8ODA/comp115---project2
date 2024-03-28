import random 
import sys
import time
import os

print("$%$%$%$%%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
print('				%$ FR BLACKJACK CENTER $%')
print("$%$%$%$%%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")

# introduction to the game
print('''	\n	Welcome to one of the most tempting games that ever existed in this word!!
				    $$$ BLACKJACK $$$                    ''')

print()
print()

#animation typing
def animation(a):
	for x in a:
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.01)
 
#explaining the rules                                                             
def Intro():
	time.sleep(2)
	animation("Blackjack is a casino banked game, meaning that players compete against the house rather than each other.")
	time.sleep(2)
	print()
	animation("The objective is to get a hand total of closer to 21 than the dealer without going over 21 (busting).")
	time.sleep(2)
	print()
	print()
	animation("The two players are drwon 2 cards facing up by the dealer.")
	print()
	animation("It goes the same to the dealer but the dealer must have the first  ard faced down.")
	time.sleep(2)
	print()
	print()
	animation("On top of that, they are some other critical information that you should know!!!")
	time.sleep(2)
	print()
	print()
	animation("Blackjack is played with a conventional deck of 52 playing cards and suits don't matter.")
	print()
	animation("2 through 10 count at face value, i.e. a 2 counts as two, a 9 counts as nine.")
	print()
	animation("Face cards (Jack,Queen,King) count as 10.")
	print()
	animation("Ace can count as a 1 or an 11 depending on which value helps the hand the most.")
	animation ("Now to appreciate your choice of playing FR BLACKJACK, we give you 5000$ to start your game!\nEnjoy...\n")
	print("%$%%$%$%$$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$$%%$%$\n\n")
	
#Defining clear the screan function
def clsf():
	os.system("cls")

#Initial bet and balance of players 
bet = 0
player_balance = 5000
system_balance = 5000
Players_bet = []
system_bet = []

#starting the game with bet
def Bet():
	global bet
	global player_balance
	global system_balance
	global system_bet
	global Players_bet
	Players_bet = 0
	system_bet = 0

	print("$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
	print("$%	Here are your balance : ",player_balance,"			    $%")
	print("$%\n$%	The Elon's balance : ",system_balance,"	 		    $%")
	print("$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
	time.sleep(1.5)
	system_bet += random.randint(100,10000)
	print("\n\nHere we go,\nthe maximum sarting bet is 10000$\n")
	print("The Elon is betting ", system_bet,"$")
	
	Players_bet += int(input("\nWhat is your bet?"))
	while Players_bet >= 10000:
		print("You cannot bet more than 10000$ !")
		Players_bet= int(input("\nWhat is your bet? " ))
		
	print("\nYou bet", Players_bet,"$")
	bet += Players_bet + system_bet
	player_balance -= Players_bet
	system_balance -= system_bet
	time.sleep(3)
	#clearing the screan and get ready for the game
	clsf()

	print ("$/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\$")
	print ("$/$\$      Current tables bet : ", bet,"	     $/$\$")
	print ("$/$\$      Your balance : ", player_balance,"	     $/$\$")
	print ("$/$\$      Elon balance : ", system_balance," 	     $/$\$")
	print ("$/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\/$\$")

 
#Defining the entire deck of card
Deck_of_cards = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,"Jack","King","Queen","ACE","Jack","King","Queen","ACE","Jack","King","Queen","ACE","Jack","King","Queen","ACE"]

#For better functionality in output,every single hand(for Dealer, System, and Player) defines in a particular function

#Dealer hand function
def Hand_of_Dealer(hand):
	global DHand
	global sumhD
	
	time.sleep(1.5)
	animation("\n\nShuffling the deck ...")
	animation("\nStarting with Dealer's hand.")
	time.sleep(2)
	
	for d  in range (2):
		hand =  random.choice(Deck_of_cards)
		Deck_of_cards.remove(hand)
		DHand.append(hand)
	
		if hand in ["Jack","King","Queen"]:
			sumhD += 10 
		elif hand in [2,3,4,5,6,7,8,9,10]:
			sumhD += int(hand)
		elif hand == "ACE":
			if sumhD <= 10 :
				sumhD += 11
			else :
				sumhD += 1
				
	print ("\n\nDealer's hand : ",["***",DHand[1]])
	return DHand, sumhD
	

#Systems hand function
def Hand_of_System(hand):
	global sumhS 
	global SHand 
	
	time.sleep(1.5)
	animation("\nNow Mr. Elon ....")
	time.sleep(2)
	
	for d  in range (2):
		hand =  random.choice(Deck_of_cards)
		Deck_of_cards.remove(hand)
		SHand.append(hand)
	
		if hand in ["Jack","King","Queen"]:
			sumhS += 10 
		elif hand in [2,3,4,5,6,7,8,9,10]:
			sumhS += int(hand)
		elif hand == "ACE":
			if sumhS <= 10 :
				sumhS += 11
			else :
				sumhS += 1
				
	print ("\n\nElon's hand : ",SHand)
	print ("Sum--> ", sumhS)
	if sumhS == 21 :
		print ("--------BLACK JACK!!!--------")
	
	time.sleep (1.8)
	system_game ()
	return SHand,sumhS

#Spilit
def split_S ():
	
	global system_balance
	global system_bet
	global SHand
	
	sumsS1 = 0
	sumsS2 = 0
	splitH1 = []
	splitH2 = []

	if SHand[0] == SHand[1]:
		animation("Elon has a chance to split.")
		time.sleep(1.5)
		splits = random.randint (1,2)
		if splits == 1 :
			animation("Elon chose to split")
			time.sleep(2)
			system_balance -= system_bet
			splitH1 = [SHand[0], random.choice(Deck_of_cards)]
			#sum of the first splited hand
			if splitH1 in ["Jack","King","Queen"]:
				sumsS1 += 10 
			elif splitH1 in [2,3,4,5,6,7,8,9,10]:
				sumsS1 += int(splitH1)
			elif splitH1 == "ACE":
				if sumsS1 <= 10 :
					sumsS1 += 11
				else :
					sumsS1 += 1
			print("Here it is\nElon;s first split : \n",splitH1,"\n","sum--> ",sumsS1)
			#hit for first split hand
			while True :
				if sumsS1 <= 10 :
					print ("Elon hits.\n")
					splitH1 = [splitH1, random.choice(Deck_of_cards)]
					if splitH1 in ["Jack","King","Queen"]:
						sumsS1 += 10 
					elif splitH1 in [2,3,4,5,6,7,8,9,10]:
						sumsS1 += int(splitH1)
					elif splitH1 == "ACE":
						if sumsS1 <= 10 :
							sumsS1 += 11
						else :
							sumsS1 += 1
					animation("....\n....")
					time.sleep(2)
					print ("Elon :\n",splitH1,"\n","Sum--> ",sumsS1)
					
				elif sumsS1 >= 18 :
					print ("\nElon stands for first split.\n")
					print ("Here it is\n : \n",splitH1,"\n","sum--> ",sumsS1)
					break
				else :
					systemchoice = random.randint (1,2)
					if systemchoice == 1 :
						print ("Elon hits.\n")
						splitH1 = [splitH1, random.choice(Deck_of_cards)]
						if SHand in ["Jack","King","Queen"]:
							sumsS1 += 10 
						elif splitH1 in [2,3,4,5,6,7,8,9,10]:
							sumsS1 += int(splitH1)
						elif splitH1 == "ACE":
							if sumsS1 <= 10 :
								sumsS1 += 11
							else :
								sumsS1 += 1
						animation("....\n....")
						time.sleep(2)
						print ("Elon :\n",splitH1,"\n","Sum--> ",sumsS1)
						
						if sumsS1 > 21 :
							print("--------Oops!--------\n--------Elon Passed 21! :(--------")
							break
						elif sumsS1 == 21 :
							print ("--------BLACK JACK!!!--------")
							break
					else :
						print ("\nElon stands for first split.\n")
						print ("Here it is\n : \n",splitH1,"\n","sum--> ",sumsS1)
						break
			
			splitH2 = [SHand[1], random.choice(Deck_of_cards)]
			#sum of the second splited hand
			if splitH2 in ["Jack","King","Queen"]:
				sumsS2 += 10 
			elif splitH2 in [2,3,4,5,6,7,8,9,10]:
				sumsS2 += int(splitH2)
			elif splitH2 == "ACE":
				if sumsS2 <= 10 :
					sumsS2 += 11
				else :
					sumsS2 += 1
			print("\nElon's second split hand -->>",splitH2,"\n","sum--> ",sumsS2)
			#hit for second split hand
			while True :
				if sumsS2 <= 10 :
					print ("Elon hits.\n")
					splitH2 = [splitH2, random.choice(Deck_of_cards)]
					if splitH2 in ["Jack","King","Queen"]:
						sumsS2 += 10 
					elif splitH2 in [2,3,4,5,6,7,8,9,10]:
						sumsS2 += int(splitH2)
					elif splitH2 == "ACE":
						if sumsS2 <= 10 :
							sumsS2 += 11
						else :
							sumsS2 += 1
					animation("....\n....")
					time.sleep(2)
					print ("Elon :\n",splitH2,"\n","Sum--> ",sumsS2)
					
				elif sumsS2 >= 18 :
					print ("\nElon stands for first split.\n")
					print ("Here it is\n : \n",splitH2,"\n","sum--> ",sumsS2)
					break
				else :
					systemchoice = random.randint (1,2)
					if systemchoice == 1 :
						print ("Elon hits.\n")
						splitH2 = [splitH2, random.choice(Deck_of_cards)]
						if splitH2 in ["Jack","King","Queen"]:
							sumsS2 += 10 
						elif splitH2 in [2,3,4,5,6,7,8,9,10]:
							sumsS2 += int(splitH2)
						elif splitH2 == "ACE":
							if sumsS2 <= 10 :
								sumsS2 += 11
							else :
								sumsS2 += 1
						animation("....\n....")
						time.sleep(2)
						print ("Elon :\n",splitH2,"\n","Sum--> ",sumsS2)
						
						if sumsS2 > 21 :
							print("--------Oops!--------\n--------Elon Passed 21! :(--------")
							break
						elif sumsS2 == 21 :
							print ("--------BLACK JACK!!!--------")
							break
					else :
						print ("\nElon stands for first split.\n")
						print ("Here it is\n : \n",splitH2,"\n","sum--> ",sumsS2)
						break

		else :
			animation("\nElon keeps his hands.\n")
						


#Game ( Hit or Stand decision for the system)
def system_game ():
	global sumhS
	global SHand
	global system_balance
	global system_bet
	#calling split function
	split_S ()
	
	#hit for system(the reason behind calling this function into the system_game function is to avoid errors for returning variables)
	def hitsystem():
		global sumhS
		global SHand
		
		SHand = [SHand, random.choice(Deck_of_cards)]
		if SHand[1] in ["Jack","King","Queen"]:
			sumhS += 10 
		elif SHand[1] in [2,3,4,5,6,7,8,9,10]:
			sumhS += int(SHand[1])
		elif SHand[1] == "ACE":
			if sumhS <= 10 :
				sumhS += 11
			else :
				sumhS += 1
		animation("....\n....")
		time.sleep(2)
		print ("Elon :\n",SHand,"\n","Sum--> ",sumhS)

		return SHand,sumhS

	while True :
		#Double for system
		if sumhS < 18 :
			Dchoice = random.randint(1,10)
			if Dchoice == 3 :
				animation("Very well\nElon chose Dubble....\n")
				system_bet += system_bet*2
				system_balance -= system_bet
				print ("$%$%$% Elon's Balance : ",system_balance,"%$%$%$")
				print ("$%$%$% Elon's Bet : ",system_bet,"%$%$%$")
				hitsystem()
				if sumhS > 21 :
					animation("--------Oops!--------\n--------Elon Passed 21! :( --------")
				elif sumhS == 21 :
					print ("--------BLACK JACK!!!--------")
				break
		elif sumhS <= 10 :
			print ("Elon hits.\n")
			hitsystem()
		elif sumhS >= 18 :
			print ("\nElon stands.\n")
			print ("Elon :\n",SHand,"\n","Sum--> ",sumhS)
			break
		else :
			systemchoice = random.randint (1,2)
			if systemchoice == 1 :
				print ("Elon hits.\n")
				hitsystem()
				if sumhS > 21 :
					print("--------Oops!--------\n--------Elon Passed 21! :(--------")
					break
				elif sumhS == 21 :
					print ("--------BLACK JACK!!!--------")
					break
			else :
				print ("\nElon stands.\n")
				print ("Elon :\n",SHand,"\n","Sum--> ",sumhS)
				break
			

#Player hand function	
def Hand_of_Player(hand):
	global sumhP
	global PHand
	
	time.sleep(1.5)
	animation("\nAnd here are your cards...")
	time.sleep(2)
	
	for d  in range (2):
		hand =  random.choice(Deck_of_cards)
		Deck_of_cards.remove(hand)
		PHand.append(hand)
	
		if hand in ["Jack","King","Queen"]:
			sumhP += 10 
		elif hand in [2,3,4,5,6,7,8,9,10]:
			sumhP += int(hand)
		elif hand == "ACE":
			if sumhP <= 10 :
				sumhP += 11
			else :
				sumhP += 1
				
	print ("\n\nYour hand : ",PHand)
	print ("Sum--> ", sumhP)
	if sumhP == 21 :
		print ("--------BlackJack !!!--------")
		time.sleep(1.8)
		Gameresult ()
	else :
		player_game ()
		
	return PHand,sumhP
	
#Spilit for player
def split_P ():
	
	global player_balance
	global Players_bet
	global PHand
	
	sumsP1 = 0
	sumsP2 = 0
	splitHP1 = []
	splitHP2 = []
	
	if PHand[0] == PHand[1]:
		splitp = input("You have chnace of split.\nSplit? ").lower().strip()
		if splitp == "split" or splitp == "s":
			player_balance -= Players_bet
			splitHP1 = [PHand[0], random.choice(Deck_of_cards)]
			#sum of the first splited hand
			if splitHP1 in ["Jack","King","Queen"]:
				sumsP1 += 10 
			elif splitHP1 in [2,3,4,5,6,7,8,9,10]:
				sumsP1 += int(splitHP1)
			elif splitHP1 == "ACE":
				if sumsP1 <= 10 :
					sumsP1 += 11
				else :
					sumsP1 += 1
			print ("Here you are, first split hand :\n",splitHP1,"\n","Sum--> ",sumsP1)
			
			Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
			while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s":
				Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
				
			while Player_decision == "hit" or Player_decision == "h" or Player_decision == "stand" or Player_decision == "s":
				if Player_decision == "hit" or Player_decision == "h" :
					time.sleep(1)
					splitHP1 = [splitHP1, random.choice(Deck_of_cards)]
					if splitHP1 in ["Jack","King","Queen"]:
						sumsP1 += 10 
					elif splitHP1 in [2,3,4,5,6,7,8,9,10]:
						sumsP1 += int(splitHP1)
					elif splitHP1 == "ACE":
						if sumsP1 <= 10 :
							sumsP1 += 11
						else :
							sumsP1 += 1
					print ("Here you are :\n",splitHP1,"\n","Sum--> ",sumsP1)
					if sumsP1 > 21 :
						animation("--------Oops!--------\n--------You Passed 21! :(--------")
						time.sleep(1.8)
						break
					elif sumsP1 == 21 :
						animation ("--------BlackJack !!!--------")
						time.sleep(1.8)
						break
				elif Player_decision == "stand" or Player_decision == "s":
					time.sleep(1.8)			
					break
				Player_decision = input ("\nDo want to Hit or Stand?  ").lower().strip()
				while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s":
					Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
			
			splitHP2 = [PHand[1], random.choice(Deck_of_cards)]
			#sum of the second splited hand
			if splitHP2 in ["Jack","King","Queen"]:
				sumsP2 += 10 
			elif splitHP2 in [2,3,4,5,6,7,8,9,10]:
				sumsP2 += int(splitHP2)
			elif splitHP2 == "ACE":
				if sumsP2 <= 10 :
					sumsP2 += 11
				else :
					sumsP2 += 1
			print ("\nyour second split hand -->",splitHP2,"\n","sum--> ",sumsP2,"\n")
			
			Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
			while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s":
				Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
				
			while Player_decision == "hit" or Player_decision == "h" or Player_decision == "stand" or Player_decision == "s":
				if Player_decision == "hit" or Player_decision == "h" :
					time.sleep(1)
					splitHP2 = [splitHP2, random.choice(Deck_of_cards)]
					if splitHP2 in ["Jack","King","Queen"]:
						sumsP2 += 10 
					elif splitHP2 in [2,3,4,5,6,7,8,9,10]:
						sumsP2 += int(splitHP2)
					elif splitHP2 == "ACE":
						if sumsP2 <= 10 :
							sumsP2 += 11
						else :
							sumsP2 += 1
					print ("Here you are :\n",splitHP2,"\n","Sum--> ",sumsP2)
					if sumsP2 > 21 :
						animation("--------Oops!--------\n--------You Passed 21! :(--------")
						time.sleep(1.8)
						results_playerS_split()
						break
					elif sumsP2 == 21 :
						animation ("--------BlackJack !!!--------")
						time.sleep(1.8)
						results_playerS_split()
						break
				elif Player_decision == "stand" or Player_decision == "s":
					time.sleep(1.8)
					results_playerS_split()
					break
				Player_decision = input ("\nDo want to Hit or Stand?  ").lower().strip()
				while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s":
					Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()
		else:
			animation("\nLet's continue then.\n")

#Game ( Hit or Stand decision for the player)
def player_game ():
	global sumhP
	global PHand
	global player_balance
	global Players_bet
	
	#calling split function
	split_P ()
	
	Player_decision =  input ("\nDo want to Hit , Stand or double!!?   ").lower().strip()
	while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s" and Player_decision != "double" and  Player_decision != "d":
		Player_decision =  input ("\n!?!?!?!?\nDo want to Hit , Stand or double!!?  ").lower().strip()
		
	while Player_decision == "hit" or Player_decision == "h" or Player_decision == "stand" or Player_decision == "s" or Player_decision == "double" or  Player_decision == "d":
		if Player_decision == "double" or Player_decision == "d" :
			time.sleep(1)
			animation("Alright,\nYou chose Dubble....\n")
			Players_bet += Players_bet*2
			player_balance -= Players_bet
			print ("$%$%$% Your Balance : ",player_balance,"%$%$%$")
			print ("$%$%$% Your Bet : ",Players_bet,"%$%$%$")
			
			PHand = [PHand, random.choice(Deck_of_cards)]
			if PHand[1] in ["Jack","King","Queen"]:
				sumhP += 10 
			elif PHand[1] in [2,3,4,5,6,7,8,9,10]:
				sumhP += int(PHand[1])
			elif PHand[1] == "ACE":
				if sumhP <= 10 :
					sumhP += 11
				else :
					sumhP += 1
				print ("Here you are :\n",PHand,"\n","Sum--> ",sumhP)
				Gameresult ()
				break
			if sumhP > 21 :
				print("--------Oops!--------\n--------You Passed 21! :(--------")
				time.sleep(1.8)
				Gameresult ()
				break
			elif sumhP == 21 :
				print ("--------BlackJack !!!--------")
				time.sleep(1.8)
				Gameresult ()
				break
		
		elif Player_decision == "hit" or Player_decision == "h" :
			time.sleep(1)
			PHand = [PHand, random.choice(Deck_of_cards)]
			if PHand[1] in ["Jack","King","Queen"]:
				sumhP += 10 
			elif PHand[1] in [2,3,4,5,6,7,8,9,10]:
				sumhP += int(PHand[1])
			elif PHand[1] == "ACE":
				if sumhP <= 10 :
					sumhP += 11
				else :
					sumhP += 1
			print ("Here you are :\n",PHand,"\n","Sum--> ",sumhP)
			if sumhP > 21 :
				print("--------Oops!--------\n--------You Passed 21! :(--------")
				time.sleep(1.8)
				Gameresult ()
				break
			elif sumhP == 21 :
				print ("--------BlackJack !!!--------")
				time.sleep(1.8)
				Gameresult ()
				break
		elif Player_decision == "stand" or Player_decision == "s":
			time.sleep(1.8)
			Gameresult ()
			break
		Player_decision = input ("\nDo want to Hit or Stand?  ").lower().strip()
		while Player_decision != "hit" and Player_decision != "h" and Player_decision != "stand" and  Player_decision != "s":
			Player_decision =  input ("\nDo want to Hit or Stand?  ").lower().strip()

def results_playerS_split():
	global sumhD
	global splitHP1
	global sumsP1
	global sumsP2
	global splitHP2
	global PHand
	global player_balance
	global Players_bet
	global splitp
	if PHand[0] == PHand[1]:
		if splitp == "split" or splitp == "s":
			animation("Your first split hand :\n")
			#evaluating results for the first split hand of player
			if sumsP1 > 21 :
				print("\nYour hand --> ",splitHP1,"Sum--> ", sumsP1)
				time.sleep(1.3)
				animation("--------You BUSTED--------\n")
			elif sumsP1 == 21 and sumhD < 21:
				print("\nYour hand --> ",splitHP1,"Sum--> ", sumsP1)
				time.sleep(1.3)
				animation("\\\\  Blackjack!!! \\\\\n")
				player_balance += (Players_bet)*2
			elif sumsP1 > sumhD :
				print("\nYour hand --> ",splitHP1,"Sum--> ", sumsP1)
				time.sleep(1.3)
				animation("--------You WON---------\n")
				player_balance += (Players_bet)*2
			elif sumsP1 < sumhD :
				print("\nYour hand --> ",splitHP1,"Sum--> ", sumsP1)
				time.sleep(1.3)
				animation("\n--------You BUSTED--------\n")
			time.sleep(1.7)
			animation("Your second split hand :\n")
			time.sleep(1.3)
			#evaluating results for the second split hand of player
			if sumsP2 > 21 :
				print("\nYour hand --> ",splitHP2,"Sum--> ", sumsP2)
				time.sleep(1.3)
				animation("--------You BUSTED--------\n")
			elif sumsP2 == 21 and sumhD < 21:
				print("\nYour hand --> ",splitHP2,"Sum--> ", sumsP2)
				time.sleep(1.3)
				animation("\\\\  Blackjack!!! \\\\\n")
				player_balance += (Players_bet)*2
			elif sumsP2 > sumhD :
				print("\nYour hand --> ",splitHP2,"Sum--> ", sumsP2)
				time.sleep(1.3)
				animation("--------You WON---------\n")
				player_balance += (Players_bet)*2
			elif sumsP2 < sumhD :
				print("\nYour hand --> ",splitHP2,"Sum--> ", sumsP2)
				time.sleep(1.3)
				animation("\n--------You BUSTED--------\n")

def resultS_System_Split():
	global sumhD
	global splitH1
	global sumsS1
	global sumsS2
	global splitH2
	global SHand
	global system_balance
	global system_bet
	global splits
	if SHand[0] == SHand[1]:
		if splits == 1 :
			animation("Elon's first split hand :\n")
			time.sleep(1.3)
			#evaluating results for the first split hand of player
			if sumsS1 > 21 :
				print("\nElon's hand --> ",splitH1,"Sum--> ", sumsS1)
				time.sleep(1.3)
				animation("--------Elon's BUSTED--------\n")
			elif sumsS1 == 21 and sumhD < 21:
				print("\nElon's hand --> ",splitH1,"Sum--> ", sumsS1)
				time.sleep(1.3)
				animation("\\\\  Blackjack!!! \\\\\n")
				system_balance += (system_bet)*2
			elif sumsS1 > sumhD :
				print("\nElon's hand --> ",splitH1,"Sum--> ", sumsS1)
				time.sleep(1.3)
				animation("--------Elon's WON---------\n")
				system_balance += (system_bet)*2
			elif sumsS1 < sumhD :
				print("\nYour hand --> ",splitH1,"Sum--> ", sumsS1)
				time.sleep(1.3)
				animation("\n--------Elon's BUSTED--------\n")
			time.sleep(1.7)	
			animation("Elon's second split hand :\n")
			time.sleep(1.3)
			#evaluating results for the second split hand of player
			if sumsS2 > 21 :
				print("\nElon's hand --> ",splitH2,"Sum--> ", sumsS2)
				time.sleep(1.3)
				animation("--------Elon's BUSTED--------\n")
			elif sumsS2 == 21 and sumhD < 21:
				print("\nElon's hand --> ",splitH2,"Sum--> ", sumsS2)
				time.sleep(1.3)
				animation("\\\\  Blackjack!!! \\\\\n")
				system_balance += (system_bet)*2
			elif sumsS2 > sumhD :
				print("\nElon's hand --> ",splitH2,"Sum--> ", sumsS2)
				time.sleep(1.3)
				animation("--------Elon's WON---------\n")
				system_balance += (system_bet)*2
			elif sumsS2 < sumhD :
				print("\nElon's hand --> ",splitH2,"Sum--> ", sumsS2)
				time.sleep(1.3)
				animation("\n--------Elon's BUSTED--------\n")


def results_player():
	
	global sumhD
	global sumhS
	global DHand
	global PHand
	global Player_decision
	global player_balance
	global Players_bet
	animation("You :\n")
	#evaluating results for the player
	if sumhP > 21 :
		print("\nYour hand --> ",PHand,"Sum--> ", sumhP)
		animation("--------You BUSTED--------\n")
	elif sumhP == 21 and sumhD < 21:
		print("\nYour hand --> ",PHand,"Sum--> ", sumhP)
		animation("\\\\  Blackjack!!! \\\\\n")
		player_balance += (Players_bet)*2
	elif sumhP > sumhD :
		print("\nYour hand --> ",PHand,"Sum--> ", sumhP)
		animation("--------You WON---------\n")
		player_balance += (Players_bet)*2
	elif sumhP < sumhD :
		print("\nYour hand --> ",PHand,"Sum--> ", sumhP)
		animation("\n--------You BUSTED--------\n")
	elif sumhD and sumhP and sumhS == 21 :
		print("\nYour hand --> ",PHand,"Sum--> ", sumhP)
		print("\nElon's",SHand,"Sum--> ", sumhS)
		animation("\n--------Pushed--------\n")
	

def Resulti ():
	global sumhD
	global sumhS
	global DHand
	global SHand
	global system_balance
	global system_bet

	animation("Elon's Game :\n")
	#evaluating results for the system
	if sumhS > 21 :
		print("\nElon's",SHand,"Sum--> ", sumhS)
		animation("\n--------Elon BUSTED--------\n")
		results_player()
	elif sumhS == 21 and sumhD < 21:
		print("\nElon's",SHand,"Sum--> ", sumhS)
		animation("\n\\\\  Elon Blackjack!!! \\\\\n")
		system_balance += (system_bet)*2
		results_player()
	elif sumhS > sumhD :
		print("\nElon's",SHand,"Sum--> ", sumhS)
		animation("\n--------Elon WON---------\n")
		system_balance += (system_bet)*2
		results_player()
	elif sumhS < sumhD :
		print("\nElon's",SHand,"Sum--> ", sumhS)
		animation("\n--------Elon BUSTED--------\n")
		results_player()
	
#Final result of the game
def Gameresult ():
	#at the end, we need to define all variables for the results
	global sumhD
	global sumhS
	global sumhP
	global DHand
	global PHand
	global SHand
	global Player_decision
	global player_balance
	global system_balance
	global system_bet
	global Players_bet 

	print("\n\n\n\n\n\n$%$%$%$%$%$%$%$%$$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
	animation("Alright,let's see who got the money!!!\n\n")
	#Dealer card reveals
	print ("Dealer hand \n-->> ",DHand,"\n","Sum--> ",sumhD)
	time.sleep(1)

	if sumhD >= 17 :
		print("Dealer stands.\n")
		resultS_System_Split()
		results_playerS_split()
		Resulti ()
	else :
		while sumhD <= 16 :
			print("Dealer would hit...\n")
			DHand = [DHand, random.choice(Deck_of_cards)]
			if DHand[1] in ["Jack","King","Queen"]:
				sumhD += 10 
			elif DHand[1] in [2,3,4,5,6,7,8,9,10]:
				sumhD += int(DHand[1])
			elif DHand[1] == "ACE":
				if sumhD <= 10 :
					sumhD += 11
				else :
					sumhD += 1
			print ("Dealers hand :\n",DHand,"\n","Sum--> ",sumhD)
		if sumhD > 21 :
			animation ("--------Dealer BUSTED--------\n")
			if sumhP and sumhS < 21 :
				player_balance += (Players_bet)*2
				system_balance += (system_bet)*2
				resul1 = animation("\n--------Players WON--------\n")
				return resul1
		elif sumhD == 21 :
			if sumhP and sumhS < 21 :
				player_balance += (Players_bet)*2
				system_balance += (system_bet)*2
				resul2 = animation("\n--------Dealer WON--------\n")
				return resul2
				
		resultS_System_Split()
		results_playerS_split()
		Resulti ()

#Intro()
#before start playing, the player could add to his wallet
print ("Before we start, you can load your wallet. For new mebers there is a 500,000$ limit.")

while True:
    try:
        player_loading = int(input("How much do you want to add? (Remember, you can go with your 5000$)"))
        break  
    except ValueError:
        print("Invalid input. Please enter a number.")

while player_loading > 500000 :
	player_loading = int(input("\nWOOOW, someones feeling lucky tonight!\nUp to 500,000, how much do you want to add? (Remember, you can go with your 5000$)"))
time.sleep(1.6)
animation("\n\nWaiting for Elon to load his wallet... ")
player_balance += player_loading
time.sleep(1.6)
system_loading = random.randint(10000,1000001)
print("Elon loaded ",system_loading,"$")
system_balance += system_loading
time.sleep(2)

PlayAgain = "yes"
while PlayAgain == "yes" or PlayAgain =="y" :
	DHand = []
	SHand = []
	PHand = []
	sumhD = 0
	sumhS = 0
	sumhP = 0
	clsf()
#Calling the Game !!!!!!!	
	Bet()
	DHand = Hand_of_Dealer(DHand)
	SHand = Hand_of_System(SHand)
	PHand = Hand_of_Player(PHand)
	
	print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*")
	PlayAgain = input ("\n\nSo do you wish to play again?").lower().strip()
	
clsf()
animation("-----------------Thank you-----------------\n\n\n\n\n\n\n")
print("$%$%$%$%%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
animation('				%$ FR BLACKJACK CENTER $%')
print("\n$%$%$%$%%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")
input()
