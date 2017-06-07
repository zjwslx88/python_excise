#reverse word order
import os 
import numpy


def reverseList(list):
	reverseList = []

	for i in range(0, len(list)):
	 	reverseList.append(list[len(list) - i-1])

	return reverseList


def main():
	samplelist= input('Enter your string: ')

	newList = reverseList(samplelist.split(" "))

	baba = ' '.join(newList)


	print "The new list is: ", baba



if __name__ == "__main__":
	main()