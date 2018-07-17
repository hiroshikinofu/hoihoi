# データの数だけ関数を呼び出す
# Python3

import chap4func
# モジュール「chap4func」を取り込め

data = [
{'name' : '山本', 'bill' : 40000, 'crg' : True},
{'name' : '吉田', 'bill' : 25000, 'crg' : False}
]
# リスト[
# 辞書｛キー「name」と文字列「山本」、キー「bill」と数値40000、キー「crg」とブール値True｝、
# 辞書｛キー「name」と文字列「吉田」、キー「bill」と数値25000、キー「crg」とブール値False｝
# ]を変数dataに入れろ

for rec in data:
# 変数data内の要素を変数recに順次入れる間、以下を繰り返せ

    bill = rec['bill']
# 変数recのキー「bill」を変数billに入れろ

    if rec['crg'] :     
        bill = chap4func.add_charge(bill)
# もしも変数recのキー「bill」が真なら以下を実行せよ
    # 変数billを指定してモジュール「chap4func」のadd_change関数を呼び出せ

       
    chap4func.create_mail(
    rec['name'], bill )
# 変数recのキー「name」と変数billを指定してモジュール「chap4func」のcreate_mail関数を呼び出せ
