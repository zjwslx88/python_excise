#Element search

import os 
import numpy
import random
import string

def findElement(list, number):

#Binary Search
	
	lo, hi = 0, len(list)-1

	while lo <= hi:
		mid = (lo + hi) /2
		if number > list[mid]:
			lo = mid + 1
		elif number < list[mid]:
			hi = mid -1
		else: return True

	return False




def main():

	list = input("Enter a list: ")
	number = input("Enter a number: ")

	listTemp = sorted(list)

	print findElement(listTemp,number)



if __name__ == "__main__": main()