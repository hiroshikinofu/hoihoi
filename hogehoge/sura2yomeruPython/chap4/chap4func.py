# メール定型文の受信者に任意の文字列を差し込む
# python3

def create_mail(recv, bill):
# create_mailという名前で、引数recvと引数billを受けとる以下の内容の関数を作る
    
    tmp = '''{}様
PT企画の斉藤です。
今月の請求書は{}円です。
'''
# 変数tmpに次の三重クォート文字列を入れろ
# 『{}様
# PT企画の斉藤です。
# 今月の請求額は{}円です。』
    
    msg = tmp.format(recv, bill)
# 変数tmpに対して、引数recvと引数billを差し込んだ結果を変数msgに入れろ

    print(msg)
# 変数msgを表示しろ

# 元の値に7%を上乗せする関数を定義する
def add_charge(bill):
    return int(bill * 1.07)
    # add chaegeという名前で、引数billを受けとる以下の内容の関数を作る
    # 引数billに数値1.07を掛けた結果を整数化して呼び出し元に返せ


