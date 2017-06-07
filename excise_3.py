import numpy
import os

def main():
	num = input("Enter a number: ")
	divisor=[]
	b=2
	while b < num:
		if num%b == 0:
			divisor.append(b)
		b = b+1

	print divisor



if __name__=="__main__":
	main()