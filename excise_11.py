#List Remove Duplicates
import os 
import numpy

''' There are just elements. 
There are no repeat elements in sets.
You can convert between sets and lists very easily.'''

def removeDup(samplelist):

	 return [-x for x in samplelist]


def setOp(set):

	newset = set()

	for x in set: newset.add(x-2*x)

	return newset



def main():
	samplelist= input('Enter your list: ')

	newList = removeDup(samplelist)

	print "The new list is: ", newList



if __name__ == "__main__":
	main()