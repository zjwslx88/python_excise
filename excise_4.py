import os
import numpy
import random

def main():

	a = random.sample(range(90), 10)
	print a
	b = random.sample(range(100), 13)
	print b
	ert=[c for c in a for d in b if c==d]
	print 'Common elements are : ', ert
	fea=[c for c in a[:7]]
	print 'The first 7 elements in a are : ', fea

		


if __name__=="__main__":
	main()