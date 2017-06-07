#Draw a game board
# -*- coding: utf-8 -*-

import os 
import numpy
import random
import string

def isOdd(number):
	if number%2 ==1:
		return True
	return False


def main():

	size = input("Enter the size of a board: ")

	if isOdd(size):

		i =0

		while i < size:
			print  (' ---'*size)
			print  ('|   '*(size+1))
			i += 1
		print (' ---'*size)

	else: print "please try an odd number. "



if __name__ == "__main__": main()