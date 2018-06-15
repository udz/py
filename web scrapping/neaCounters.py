# Check the NEA Counters from Third Party
import requests, bs4, pprint

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

res = requests.get('https://www.nibl.com.np/nea/')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html5lib")

elemF = soup.find("select", {"id": "ddlCounterName"}).contents

list = []

for i in range(0,len(elemF)-1):
    if (elemF[i] != '\n\t\t\t'):
        NEA_counter = find_between(str(elemF[i]),">","<")
        list.append(NEA_counter)
        
pprint.pprint(list)
print('\nTotal Counters of NEA: ' + str(len(list)-1))
