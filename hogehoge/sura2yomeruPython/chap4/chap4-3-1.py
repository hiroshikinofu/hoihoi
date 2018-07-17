# メール定型文の受信者に任意の文字列を差し込む
# python3

def create_mail(recv, bill):
# create_mailという名前で、引数reacvと引数billを受けとる以下の関数を作る

    tmp = '''{}様
PT企画の斉藤です。
今月の請求額は{}円です。
'''
# 変数tmpに次の三重クォート文字列を入れろ
# 『{}様
# PT企画の斉藤です。
# 今月の請求額は{}円です。』

    msg = tmp.format(recv, bill)
# 変数tmpに対して、引数recvと引数billを差し込んだ結果を変数msgに入れろ

    print(msg)
# 変数msgを表示しろ

create_mail('山本', 40000)
# 文字列「山本」と数値40000を指定してメールを作れ
