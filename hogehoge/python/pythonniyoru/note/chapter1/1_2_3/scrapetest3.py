# scrapetest2.pyの6行目
# 「html = urlopen("http://www.pythonscraping.com/pages/page1.html")」に
# はらんでいる２つの問題「ページがサーバ上で見つからない（または、取り出すときにエラー）」、
# 「サーバが見つからない」について、対応策を11～18行目に追加

from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null、break、あるいは他の「プランB」を実行
else:
    pass
    # プログラムは継続。注意、例外の補足でreturnかbreakしたなら、
    # else文は要らない

bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
