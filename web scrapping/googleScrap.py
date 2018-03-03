import requests, bs4
res = requests.get('https://www.google.com.np/')

res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"html5lib")


print(noStarchSoup.select('div input'))  #input element inside div
print(noStarchSoup.select('div > input'))  #input element directly inside div

noStarchSoup.select('.notice') # all elements with the css class attribute named notice
noStarchSoup.select('#author') # the element with an id attribute named author
                    
#print(noStarchSoup.select('head')) # Head element
#print(noStarchSoup.select('.sbibtd'))


