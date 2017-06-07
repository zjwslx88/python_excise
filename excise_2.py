import os 
import numpy
'''List comprehension'''

def main():
	a= [1,1,2,3,5,8,13,21,35,55,89]
	while True:
		c = input("Enter a number: ")
		print[b for b in a if b < c]  

if __name__ == "__main__":
	main()
