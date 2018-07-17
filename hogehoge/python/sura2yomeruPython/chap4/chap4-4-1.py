# 元の値に7%を上乗せする関数を定義する
def add_charge(bill):
    return int(bill * 1.07)
    # add chaegeという名前で、引数billを受けとる以下の内容の関数を作る
    # 引数billに数値1.07を掛けた結果を整数化して呼び出し元に返せ
print(add_charge(40000))
    # 数値40000を指定して手数料を追加した結果を表示しろ
