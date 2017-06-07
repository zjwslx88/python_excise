import os 
import numpy
import random

# A one opposite guess game.  

def main():

	count = 0

	guess = 50

	while True:

		print 'Let me guess... Is it %i?', guess

		tips = raw_input("give me tips: ")

		if tips == 'yes':
	
			print 'The number of guess is', count+1

			break 

		elif tips == 'high':

			guess = random.randint(guess/2,guess)

			count += 1

		elif tips == 'low':

			guess = random.randint(guess, guess + guess/2)

			count += 1

		if tips == 'exit': 
			print 'You mean quit this game.'
			break

		if tips == 'help':
			print 'A machine guess game'




if __name__=="__main__":
	main()