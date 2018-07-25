# フォルダ内のファイル一覧を取得する
# Python3

from pathlib import Path            #1
path = Path()                       #2
for filepath in path.glob('*.py'):  #3
    print(filepath)                 #4

#1 pathlibモジュールからPathオブジェクトを取り込め
    #※Pathオブジェクトの頭は大文字

#2 Pathオブジェクトを作成し、変数pathに入れろ
    #※Pathオブジェクトの頭は大文字
    
#3 文字列「*.py」を指定して変数path内のファイルを取得し、
#3 変数filepathに順次入れる間、以下を繰り返せ
    #4 変数filepathを表示しろ
