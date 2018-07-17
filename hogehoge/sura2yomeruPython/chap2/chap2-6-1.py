text = input('年齢は？')
age = int(text)
if age < 20:
    print('未成年')
elif age < 65:
    print('成人')
else:
    print('高齢者')
