#List operation
import os 
import numpy

def main():
	samplelist= input('Enter your list: ')
	newList= [samplelist[0], samplelist[len(samplelist)-1]]
	'''Either way 
	newList = []
	newList.append(samplelist[0])
	newList.append(samplelist[len(samplelst)- 1])

	'''

	print "The new list is: ", newList





if __name__ == "__main__":
	main()