import newspaper

cnn_paper = newspaper.build('http://cnn.com')
#msn_paper = newspaper.build('https://msn.com')

#for article in cnn_paper.articles:
#    print(article.url)

#for category in cnn_paper.category_urls():
#    print(category)

cnn_article = cnn_paper.articles[0]
cnn_article.download()
cnn_article.parse()
print(cnn_article.nlp())
