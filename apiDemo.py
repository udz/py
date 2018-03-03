# Minimal API interaction program

import json, requests, pprint

url = 'http://localhost:3000/users'
response = requests.get(url)
response.raise_for_status()

pythonValue = { 'name':'Bikash Koirala',
                'email':'bikash@gmail.com',
                'password':'logic333'}

pythonValue2 = { 'name':'Neelam Basnet',
                'email':'nilu@hotmail.com',
                'password':None}

stringOfJsonData = json.dumps(pythonValue)
#requests.post(url, data=pythonValue)
#print(response.json())
#requests.delete(url + '/'+'5a354df5d4e690247ce89d9f')


requests.put(url + '/' + '5a354dc8d4e690247ce89d9e', data = json.dumps(pythonValue2))

r = requests.head(url)
res = requests.options(url)

pprint.pprint(response.json())

'''
>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
'''
