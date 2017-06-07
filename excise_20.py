#File Overlap

import os 
import numpy
import random
import string



def main():

	primenumbers = 'primenumbers.txt'

	happynumbers = 'happynumbers.txt'

	f1 = open(primenumbers, 'r')

	f2 = open(primenumbers, 'r')

	list1 = []
	list2 = []


	try: 
		# add stuff here
		#print f.read()
		for primenumber in f1.readlines():
			list1.append(primenumber.strip())

		for happynumber in f2.readlines():
			list2.append(happynumber.strip())


	finally:
		f1.close()
		f2.close()

	list3 = []

	for prime in list1:
		for happy in list2:
			if prime == happy:
				list3.append(prime)
	print list3


if __name__ == "__main__": main()