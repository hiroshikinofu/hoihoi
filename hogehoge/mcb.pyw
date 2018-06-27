#! python3
# macb.pyw - クリップボードのテキストを保存・復元
# Usege:
# py.exe mcd.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# py.exe mcd.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcd.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys   #

mcb_shelf = shelve.open('mcb')  #

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1] == 'save':    #
    mcd_shelf[sys.argv[2]] = pyperclip.paste()  #
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':   #
        pyperclip.copy(str(list(mcd_shelf.keys()))) #
    elif sys.argv[1] in mcd_sheif:
        pyperclip.copy(mcd_shelf[sys.argv[1]])  #

mcb_shelf.close()
