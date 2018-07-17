# 2週間分の日付の一覧を作る
# Python3

from datetime import date, timedelta
# datetimeモジュールからdateオブジェクトとtimedeltaオブジェクトを取り込め

start = date(2018, 6, 18)
# 数値2018と数値6と数値18を指定してdateオブジェクトを作成し、変数startに入れろ

for d in range(14):
# 0～数値10直前の範囲内の整数を変数dに順次入れる間、以下を繰り返せ

    cur = start + timedelta(days=d)
    # 引数daysに変数dを指定してtimedaltaオブジェクトを作成し、
    # それを変数startに足した結果を変数curに入れろ

    print(cur)
    # 変数curを表示しろ
