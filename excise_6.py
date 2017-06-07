import os 
import numpy
import random

# A Rock Paper Scissors Game. 

def main():
	while True:
		move = raw_input("Please type 'rock, paper, scissors': ")
		computer_choice = random.randint(0,2) #0: scissors, 1: rock, 2: paper
		if move == 'scissors':
			if computer_choice == 0: print 'I choose scissors, Tie!'
			elif computer_choice == 1: print 'I choose rock, I win!'
			else: print 'I choose paper, you win!'

		if move == 'rock':
			if computer_choice == 0: print 'I choose scissors. You win!'
			elif computer_choice == 1: print 'I choose rock. We tie'
			else: print 'I choose paper. I win!'

		if move == 'paper':
			if computer_choice == 0: print 'I choose scissors. I win!'
			elif computer_choice == 1: print 'I choose rock. You win!'
			else: print 'I choose paper. We tie!'

		if move == 'quit':
			print 'you quit the game~'
			break

		else: print 'Please try again!'


if __name__=="__main__":
	main()