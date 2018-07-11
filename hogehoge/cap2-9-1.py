text = input('年齢を入力してください')
if not text.isdigit():
    プログラム中断
age = int(text)
if age < 20:
    if age >= 6 and age <=15:
        print('未成年(義務教育)')
    else:
        print('未成年')
elif age < 65:
    print('成人')
else:
    print('高齢者')
