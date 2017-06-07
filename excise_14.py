#Decode a Web Page
#Use 'requests' to get the whole HTML from the url
#and then use 'Beautifulsoup' to recode the obtained HTML
import os 
import numpy
import random
import string
from bs4 import BeautifulSoup
import requests



def main():

	url = 'https://www.google.com/finance/market_news?ei=0KA0WcjfAoiZ0ATYk6-ABQ'
	r = requests.get(url)
	r_html = r.text

	soup = BeautifulSoup(r_html, "html.parser")

	for story_heading in soup.find_all(class_="name"): 

	# for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely

	    if story_heading.a: 
	    	print(story_heading.a.text.replace("\n", " ").strip())
	    else: 
	        print(story_heading.contents[0].strip())


if __name__ == "__main__":
	main()