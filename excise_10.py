#Fibonnaci Sequence

import os 
import numpy

def main():

	while True:

		limit = input("Enter a number: ")
		#Particular scenario
		if limit == 1: print [1]
		elif limit == 2: print [1,1]

		myList = [1,1]
		number = 2

		while number < limit:
			myList.append(myList[number-1] + myList[number-2])
			number+=1
		print myList





if __name__ == "__main__":
	main()