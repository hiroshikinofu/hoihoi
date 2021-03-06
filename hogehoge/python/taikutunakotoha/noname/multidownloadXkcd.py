#! python3
# multidownloadXkcd.py - CKCDコミックをマルチスレッドでダウンロードする

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)      # ./xkcdにコミックを保存

def download_xkcd(start_comic, end_comic):  #
    for url_number in range(start_comic, end_comic):    #
    # ページをダウンロードする
    print('ページをダウンロード中 http://xkcd.com/{}...'.format(url_number))
    res = requests.get('http://xkcd.com/{}'.format(url_number))    #
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)      #

    # コミック画像のURLを見つける
    comic_elem = soup.select('#comic img')  #
    if comic_elem == []:
        print('コミック画像が見つかりませんでした。')
    else:
        comic_url = 'http:' + comic_elem[0].get('src')  #
        # 画像をダウンロードする
        print('画像をダウンロード中 {}...'.format(comic_url))
        res = requests.get(comic_url)       #
        res.raise_for_status()

        # 画像を./xkcdに保存する
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

# threadオブジェクトを生成して開始する
download_threads = []           # 全Threadオブジェクトのリスト
for i in range(1, 1400, 100):   # 14回ループし、14個のスレッドを生成
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 100))
    download_threads.append(download_thread)
    download_thread.start()

# すべてのスレッドが終了するのを待つ
for download_thread in download_threads:
    download_thread.join()
print('完了')
