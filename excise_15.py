#Cows and bulls
import os 
import numpy
import random
import string

def main():

	incode = random.randint(100,999)

	print "the incode is : ", incode

	while True:

		codeString = str(incode)

		countCow, countBull = 0, 0


		guess = input("Welcome to the Cows and Bulls Game\nEnter a number: ")


		guessString = str(guess)

		if guessString[0] == codeString[0]: countCow += 1
		if guessString[1] == codeString[1]: countCow += 1
	 	if guessString[2] == codeString[2]: countCow += 1

		if guessString[0] == codeString[1]: countBull +=1
		if guessString[0] == codeString[2]: countBull +=1
		if guessString[1] == codeString[0]: countBull +=1
		if guessString[1] == codeString[2]: countBull +=1
		if guessString[2] == codeString[1]: countBull +=1
		if guessString[2] == codeString[0]: countBull +=1

		print str(countCow)+ " Cow, " + str(countBull)+ " bull"


if __name__ == "__main__":
	main()