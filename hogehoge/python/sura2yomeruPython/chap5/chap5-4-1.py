# テキストファイルを読み込んで内容を確認する
# python3

rfile = open('sample.txt',
encoding = 'utf-8')         #1
text = rfile.read()         #2
rfile.close()               #3
print(text)                 #4

#1 文字列「sample.txt」と引数encodingに文字列「utf-8」を指定し、
#  開いた結果を変数rfileに入れろ
#2 変数rfileを読み込んだ結果を変数textに入れろ
#3 変数rfileを閉じろ
#4 変数textを表示しろ
