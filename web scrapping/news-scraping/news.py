from newspaper import Article

import pprint

from newspaper import fulltext
import requests

url = 'https://edition.cnn.com/2018/07/06/health/thai-soccer-team-oxygen-bn/index.html'
article = Article(url)
article.download()
#print(article.html)

article.parse()
print(article.title)
print(article.authors)
print(article.publish_date)
print(article.text[:150])
#pprint.pprint(article.text)
print('\n')
# Extracting fulls text from HTML file
html = requests.get(url).text
text = fulltext(html)
print(text[:150])


res = requests.get(sub.url)
if (res.status_code == 200 and 'content-type' in res.headers and res.headers.get('content-type').startswith('text/html')):
    html = res.text