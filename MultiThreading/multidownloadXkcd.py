#! python3
# multidownloadXkcd.py

import requests, os, bs4, threading

os.makedirs('MultiThreading/xkcd',exist_ok=True) # Create output directory 

def downloadXkcd(startcomic,endcomic):
    for urlNumber in range(startcomic,endcomic):
        # Download the page
        print('Downloading the page %s' %(urlNumber))
        res = requests.get('https://xkcd.com/%s' %(urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,"html5lib")
        # Find the url of comic image
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Couldn't find comic image.")
        else:
            comicURL = 'https:'+comicElem[0].get('src')
            url = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' %(comicURL))
            res = requests.get(comicURL)
            res.raise_for_status()
            # Save the image
            imageFile = open(os.path.join('MultiThreading/xkcd', os.path.basename(url)), 'wb')
            #imageFile = open(os.path.basename(url), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start thread object
downloadThreads = []
for i in range(1,200,20):  # creates 10 threads, 20 downloads in each thread
    downloadThread = threading.Thread(target=downloadXkcd,args=(i,i+19))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done!')
