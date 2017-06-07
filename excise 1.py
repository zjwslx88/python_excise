import os
import numpy

def main():
	while True:
		number = input("Could you please type one number? ")
		if number%2 == 0:
			if number%4 == 0:
				print ("Well, this number is the multiple of 4.")
			else:	 
				print ("The number you typed is a even number")
		else:
			print ("This is an odd")

if __name__ == "__main__":
	main()