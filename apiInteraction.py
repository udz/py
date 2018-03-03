
import http.client

conn = http.client.HTTPConnection("192,168,1,35:3000")

payload = "name=Laxman%20Adhikari&email=lax%40man.com&password=metoo"

headers = {
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
'Postman-Token': "e5dea485-a7e8-0d3a-4999-f73e80d83e32"
}

conn.request("GET", "users,", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


"""
from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print (kittens[559:1000])
except URLError:
    print ('No kittez. Got an error code:', e)
"""
