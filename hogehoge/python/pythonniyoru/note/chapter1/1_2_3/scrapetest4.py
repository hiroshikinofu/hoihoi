# scrapetest3.pyに「サーバに全く到達できなかった場合のチェックコードを追加

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null、break、あるいは他の「プランB」を実行
except URLError as e:
    print("The server could not be found!")
else:
    print("It Workd!")
