#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer

#site = sys.argv[1]
#page = requests.get(site)

#if page.status_code != 200
def fetching(base,site):
	urls = []
	print('fetching',site)
#	s = requests.session()
#	s.config['keep_alive'] = False
	page = requests.get(site)
	for links in BeautifulSoup(page.text,'html.parser',parse_only=SoupStrainer('a')):
		if links.has_attr('href'):
			if links['href'] != "":
				if links['href'][0] != '#' and links['href'][:3] != 'www' and links['href'][:4] != 'http' and links['href'][:2]!='//':
					if links['href'][0] != '/' :
						links['href'] = '/' + links['href']
					if links['href'][0] == '/':
						urls.append(base+links['href'])
					#else: urls.append(links['href'])

	urls = set(urls)
	urls = list(urls)


	return urls


