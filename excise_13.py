#Password Generator
import os 
import numpy
import random
import string

def passwordGen(strength):

	symbols = '!@#$%^&*+-'

	if strength == 'weak': 
		s= (''.join(random.sample(string.ascii_uppercase, random.randint(2,4))) + 
			''.join(random.sample(string.ascii_lowercase,random.randint(2,6))))
		
		return ''.join(random.sample(s, len(s)))

	elif strength == 'medium': 
		s= (''.join(random.sample(string.ascii_uppercase, random.randint(2,4))) +
				''.join(random.sample(string.ascii_lowercase,random.randint(2,6))) +
				''.join(random.sample(string.digits,random.randint(2,6))))

		return ''.join(random.sample(s, len(s)))

	elif strength == 'hard': 
		s= (''.join(random.sample(string.ascii_uppercase, random.randint(2,6))) +
				''.join(random.sample(string.ascii_lowercase,random.randint(4,6))) +
				''.join(random.sample(string.digits,random.randint(4,6))) + 
			    ''.join(random.sample(symbols,random.randint(1,2))))

		return ''.join(random.sample(s, len(s)))

	else: print "please try again"

def main():

	while True:

		strength = input("Enter the strength of your password: ")

		print passwordGen(strength)


if __name__ == "__main__":
	main()