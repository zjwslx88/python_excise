#Decode a Web Page 2
#Use 'requests' to get the whole HTML from the url
#and then use 'Beautifulsoup' to recode the obtained HTML
#read the whole text information from an article
import os 
import numpy
import random
import string
from bs4 import BeautifulSoup
import requests



def main():

	url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
	r = requests.get(url)

	soup = BeautifulSoup(r.text,"html.parser")

	for content in soup.find_all("section", class_="content-section"): 

		print content.text

	# for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely


if __name__ == "__main__":
	main()