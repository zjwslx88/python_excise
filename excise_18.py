#Element search

import os 
import numpy
import random
import string
import requests
from bs4 import BeautifulSoup



def main():

	fileName = input("Enter a file name: ")+'.txt'

	f = open(fileName, 'w+')

	url = 'https://www.google.com/finance/market_news?ei=0KA0WcjfAoiZ0ATYk6-ABQ'
	r = requests.get(url)
	r_html = r.text

	soup = BeautifulSoup(r_html, "html.parser")

	for story_heading in soup.find_all(class_="name"): 

	# for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely

	    if story_heading.a: 
	    	buff1 = (story_heading.a.text.replace("\n", " ").strip()).encode('utf-8')+'\n'
	    	f.write(buff1)
	   
	    else: 
	        buff2 = (story_heading.contents[0].strip()).encode('utf-8')+'\n'
	        f.write(buff2)

	f.close()



if __name__ == "__main__": main()