from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import sys

page_url = "http://www.di.uoa.gr/undergraduate/courses/newpps"

# Query the website and return the html
page = urlopen(page_url)

# Parse the html using beautiful soup
soup = BeautifulSoup(page, "html.parser")

content_table = []

# Finding the table elements that include the data
for table in soup.find_all("table", { "class": "views-table sticky-enabled cols-15"}):
	# In every table row try finding specific element
	for tr in table.find_all("tr"):
		try:
			if(tr.find("td", { "class": "views-field views-field-field-e" + sys.argv[2] + "-value"}).text.strip() != ''):

				title = tr.find("td", { "class": "views-field views-field-title"}).text.strip()
				value = tr.find("td", { "class": "views-field views-field-field-e" + sys.argv[2] + "-value"}).text.strip()
				
				content_table.append([title, value])
		except:
			continue

with open("./specializations/" + sys.argv[1] + ".csv", 'w', newline='') as new_file:

	csv_writer = csv.writer(new_file, delimiter=',')

	csv_writer.writerows(content_table)
