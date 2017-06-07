#Element search

import os 
import numpy
import random
import string
import requests
from bs4 import BeautifulSoup



def main():

	fileName = input("Enter a file name: ")

	f = open(fileName, 'r')

	output = set()

	try: 
		# add stuff here
		#print f.read()
		for name in f.readlines():
			output.add(name.strip())
		print output


	finally:
		f.close()



if __name__ == "__main__": main()