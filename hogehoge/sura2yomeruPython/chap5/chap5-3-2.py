# 日付一覧に曜日も表示する
# python3

from datetime import date, timedelta
# datetimeモジュールからdateオブジェクトとtimedeltaオブジェクトを取り込め

youbi = '月火水木金土日'
# 文字列「月火水木金土日」を変数youbiに入れろ

start = date(2018, 6, 18)
# 数値2018と数値6と数値18を指定してdateオブジェクトを作成し、変数startに入れろ


for d in range(14):
# 0～数値14直前の範囲内の整数を変数dに順次入れる間、以下を繰り返せ

    cur = start + timedelta(days=d)
    # 引数daysに変数dを指定したtimedaltaオブジェクトを作成し、
    # それを変数startに足した結果を変数curに入れろ

    wd = cur.weekday()
    # 変数curの曜日を調べて変数wdに入れろ

    print(cur, youbi[wd])
    # 変数curと変数youbiの要素wdを表示しろ
