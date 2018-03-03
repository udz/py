import requests, bs4
#res = requests.get('http://google.com')
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.75108419999998&lon=-73.88532059999994#.Wpo-luhuaM8')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html5lib")
print(type(soup))

#print(len(noStarchSoup.select('input[type="text"]')))
#noStarchSoup.select('div')


elemF = soup.select(".myforecast-current-lrg")
elemC = soup.select(".myforecast-current-sm")

print('Current temperature is ' + elemF[0].getText() +' & ' +elemC[0].getText())
print(elemF[0].attrs)

#print(soup.select('div > table'))
#print(soup.select('#detailed-forecast'))

'''
<div id="current_conditions_detail" class="pull-left">
		    <table>
            <tbody><tr>
            <td class="text-right"><b>Humidity</b></td>
            <td>65%</td>
            </tr>
            <tr>
            <td class="text-right"><b>Wind Speed</b></td>
            <td>NW 24 G 35 mph</td>
            </tr>
            <tr>
            <td class="text-right"><b>Barometer</b></td>
            <td>29.78 in (1008.5 mb)</td>
            </tr>
            <tr>
            <td class="text-right"><b>Dewpoint</b></td>
            <td>27°F (-3°C)</td>
            </tr>
            <tr>
            <td class="text-right"><b>Visibility</b></td>
            <td>10.00 mi</td>
            </tr>
            <tr><td class="text-right"><b>Wind Chill</b></td><td>27°F (-3°C)</td></tr>            <tr>
            <td class="text-right"><b>Last update</b></td>
            <td>
                3 Mar 12:51 am EST            </td>
            </tr>
		    </tbody></table>
		</div>

'''
