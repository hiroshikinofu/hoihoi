# ページ内に表示されている「$15.00」の価格が表示されたオブジェクトを表示する
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj =BeautifulSoup(html)
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"
                         }).parent.previous_sibling.get_text())
