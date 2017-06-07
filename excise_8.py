import os 
import numpy
import random

# A one guess game.  

def main():
	value = 1

	while True:
		here = input("Enter a number: ")
		if here == 2: print "That is a prime. "
		# Other senario
		elif here != 2:
			for i in range(2, here):
				if here%i ==0: 
					value = 0

		if value == 0: 
			print "Not a Prime"
			value = 1
		elif value == 1: print "Prime" 




if __name__=="__main__":
	main()