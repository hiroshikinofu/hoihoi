# 「for」の出現回数を調べる
# Python3

from pathlib import Path                #1
path = Path()                           #2
for filepath in path.glob('*.py'):      #3
    rfile = open(filepath,              #4
     encoding='utf-8')                  #4    
    text = rfile.read()                 #5
    rfile.close()                       #6
    cnt = text.count('for')             #7
    print(filepath, cnt)                #8

#1 pathlibモジュールからPathオブジェクトを取り込め
    #※Pathオブジェクトの頭は大文字

#2 Pathオブジェクトを作成し、変数pathに入れろ
    #※Pathオブジェクトの頭は大文字
    
#3 文字列「*.py」を指定して変数path内のファイルを取得し、
#3 変数filepathに順次入れる間、以下を繰り返せ
    #4 変数filepathと引数encodingに文字列「utf-8」を指定し、
    #4 開いた結果を変数rfileに入れろ
    #5 変数rfileを読み込んだ結果を変数textに入れろ
    #6 変数rfileを閉じろ
    #7 変数textの中の文字列「for」を教えて、その結果を変数cntに入れろ
    #8 変数filepathと変数cntを表示しろ
