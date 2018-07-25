# 置換後の文字列を保存する
# python3

rfile = open('sample.txt',
encoding = 'utf-8')                 #1
text = rfile.read()                 #2
rfile.close()                       #3
text = text.replace('。', '～♪')   #4
print(text)                         #5
wfile = open('output.txt',          #6
 mode = 'w', encoding='utf-8')      #6
wfile.write(text)                   #7
wfile.close()                       #8

#1 文字列「sample.txt」と引数encodingに文字列「utf-8」を指定し、
#1 開いた結果を変数rfileに入れろ
#2 変数rfileを読み込んだ結果を変数textに入れろ
#3 変数rfileを閉じろ
#4 変数textの文字列「。」を文字列「～♪」に置換した結果を変数textに入れろ
#5 変数textを表示しろ
#6 文字列「output.txt」と引数modeに文字列「w」と
#6 引数encodingに文字列「utf-8」を指定し、開いた結果を変数wfileに入れろ
#7 変数textを変数wfileに書き込め
#8 変数wfileを閉じろ
