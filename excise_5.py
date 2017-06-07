import os
import numpy
import random


def main():
	while True:
		word = raw_input("Enter a string: ")

		for i in range(len(word)):
			if word[i] == word[len(word)-1-i]:
				value = 0

			else: value =1
		if value == 0: print "True"
		else: print "False"




		


if __name__=="__main__":
	main()