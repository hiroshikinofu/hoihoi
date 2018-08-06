from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll(text="the prince")
# html変数のURLページ上に「the prince」が何回タグに含まれていたかをカウントしろ
print(len(nameList))
