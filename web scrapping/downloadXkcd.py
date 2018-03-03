#! python3
# downloadXkcd.py

import requests, os, bs4

url = 'https://xkcd.com'


while not url.endswith('#'):

    res = requests.get(url)

    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,"html5lib")
    comicElem = soup.select("#comic img")

    if comicElem == []:
        print("Couldn't find comic image.")
    else:
        try:
            # imagelink
            comicURL = 'https:'+comicElem[0].attrs.get('src')
            print('Downloading image ' + comicURL)
            resC = requests.get(comicURL)
            resC.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevElem = soup.select("li > a['rel='prev'']")
            prevURL ='https://xkcd.com'+prevElem[0].attrs.get('href')
            print(prevURL)
            url = prevURL
            continue
    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
    for chunk in resC.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # previous URL    
    prevElem = soup.select("li > a['rel='prev'']")
    prevURL ='https://xkcd.com'+prevElem[0].attrs.get('href')
    print(prevURL)
    url = prevURL
    
print('Done!')
