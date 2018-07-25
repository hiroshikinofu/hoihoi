# 複数のキーワードの出現数の合計を求められるようにする
# Python3

from pathlib import Path                    #1
terms = {'for' : 0, 'if' : 0, 'else' : 0}   #2
path = Path()                               #3
for filepath in path.glob('*.py'):          #4
    
    rfile = open(filepath,                  #5
     encoding='utf-8')                      #5
    
    text = rfile.read()                     #6
    rfile.close()                           #7
    for term in terms:                      #8
        cnt = text.count(term)              #9
        terms[term] += cnt                  #10
print(terms)                                #11

#1 pathlibモジュールからPathオブジェクトを取り込め
    #※Pathオブジェクトの頭は大文字

#2 辞書{キー「for」と数値0,キー「if」と数値0、キー「else」と数値0}を
#2 変数termsに入れろ

#3 Pathオブジェクトを作成し、変数pathに入れろ
    #※Pathオブジェクトの頭は大文字
    
    
#4 文字列「*.py」を指定して変数path内のファイルを取得し、
#4 変数filepathに順次入れる間、以下を繰り返せ
    
    #5 変数filepathと引数encodingに文字列「utf-8」を指定し、
    #5 開いた結果を変数rfileに入れろ
    
    #6 変数rfileを読み込んだ結果を変数textに入れろ
    #7 変数rfileを閉じろ
    #8 変数termsの中のキーを変数termに順次入れる間、以下を繰り返せ
        #9 変数textの中の変数termを数えて、その結果を変数cntに入れろ
        #10 変数termsのキーtermに変数cntを足して入れろ
#11 変数termsを表示しろ
