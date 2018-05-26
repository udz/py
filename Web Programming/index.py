"""

    Page Templating with Python 🌐🐍
    GitHub :: PCabralSoftware - 2K18 - Twitter :: @pedrogcabral

"""

from browser import document
from browser import html
from browser.template import Template

pageName = "Python 🐍"

articleContent = open('news_file.txt').read()
articleTitle = articleContent.split('\n', 1)[0]
articleText = articleContent.split('\n', 1)[1]

article = [html.H1('{title}', Id='art_title'), html.P('{text}', Id='art_content')]

nav = html.DIV([html.H1('{title}', Id='title'), html.H2('☰', Id='navbtn')], Class="nav")

cnt = html.DIV(html.DIV(article, Class="article"), Class="content")

ftr = html.DIV([html.P('Copyright {} 2018 - All rights reserved.'.format(pageName))], Class="footer")

document <= [nav, cnt, ftr]

Template(document['title']).render(title=pageName)
Template(document['art_title']).render(title=articleTitle)
Template(document['art_content']).render(text=articleText)