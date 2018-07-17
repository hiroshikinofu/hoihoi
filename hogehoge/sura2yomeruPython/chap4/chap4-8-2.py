# 復習問題
# 問題2:請求額がマイナスのときは0を返す
# Python3

def add_charge(bill):
# add_chargeという名前で引数billを受けとる以下の内容の関数を作る

    if bill < 0:
# もしも「引数billが数値0より小さい」が真ならば以下を実行しろ

        return 0
# 数値0を呼び出し元に戻せ

    return int(bill * 1.07)
# 引数billに数値1.07を掛けた結果を整数化して呼び出し元に返せ


print(add_charge(-1000))
# 数値-1000を指定して手数料を追加した結果を表示しろ
