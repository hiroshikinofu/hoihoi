# 複数人のデータをリストにまとめる

data = [
{'name' : '山本', 'bill' : 40000, 'crg' : True},
{'name' : '吉田', 'bill' : 25000, 'crg' : False}
]
# リスト[
# 辞書{キー「name」と文字列「山本」、キー「bill」と数値40000、キー「crg」とブール値True}、
# 辞書{キー「name」と文字列「吉田」、キー「bill」と数値25000、キー「crg」とブール値False}
# ]を変数dataに入れろ

print(data[1]['name'])
# 変数dataの要素1のキー「name」を表示しろ

print(data[1]['bill'])
# 変数dataの要素1のキー「bill」を表示しろ

