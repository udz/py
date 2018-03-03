import webbrowser, requests
street = '870+Valencia+St+San+Francisco+CA'
#webbrowser.open('https://www.google.com/maps/place/' + street +'/')

res = requests.get('https://google.com')
print(type(res))

if (res.status_code == requests.codes.ok):
    print(len(res.text))
   # print(res.text[:1000])

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
