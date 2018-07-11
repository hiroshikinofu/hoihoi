text = input('年齢は?')
if text.isdigit():
    age = int(text)
    if age < 20:
        print('未成年')
    elif age < 30:
        print('青年')
    elif age < 45:
        print('中年')
    elif age < 75:
        print('老人')
    else:
        print('奇跡')
