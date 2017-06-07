import os 
import numpy
import random

# A one guess game.  

def main():

	star = random.randint(1,9) #randomly generate a number
	count = 0

	while True:
		guess = input("Enter a number: ")
		if guess == star:
			count += 1
			print 'You got it ! You have tried: ', count
			count = 0
		elif guess > star:
			count += 1
			print 'Too high, please try again!'

		else: 
			count += 1
			print 'Too low, please try again!'

		if guess == 'exit': 
			print 'You mean quit this game.'
			break



if __name__=="__main__":
	main()