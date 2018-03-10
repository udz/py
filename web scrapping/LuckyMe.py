#! python3
#lucky.py
# This program asks user to enter a search term, googles it and opens first 5 links in the default web browser

import requests, sys, webbrowser, bs4

term = input('Enter Term to Google: ')

print('Googling...')
res = requests.get('https://www.google.com.np/search?q='+term)
res.raise_for_status


#print(res.status_code, requests.codes.ok)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

