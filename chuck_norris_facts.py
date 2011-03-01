#!/usr/bin/python
import urllib2, time
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

# for local testing, as to not hit the web server
#html = open('page.html').read()
#soup = BeautifulSoup(html)

# 674 pages last time I checked. Oddly enough, their pages seem zero-based. Additionally, if you 
# substitute an arbitrary number, outside of the range of pages, you'll get data back instead
# of 404. I'm not sure why they're doing this.
for page_num in range(0,674):
	url = 'http://www.chucknorrisfacts.com/all-chuck-norris-facts?page=%d' % page_num
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)

	entries = soup.findAll("li","views-row")
	for entry in entries:
		
		# use BeautifulStoneSoup to remove any HTML-escaped text that BS returns.
		the_quote = BeautifulStoneSoup(entry.div.text, 
		                   convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]
		
		# print it to stdout. I just redirect the program's output to a file.
		print the_quote.encode('utf-8')
	# be a good citizen and wait a few seconds before visiting the next page
	time.sleep(6)