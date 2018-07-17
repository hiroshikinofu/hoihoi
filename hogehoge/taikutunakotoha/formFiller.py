#! python3
# formFiller.py - フォームの自動入力

import pyautogui, time

# 以下の値は実際に調べたものに置き換えること。
name_field = (565, 338)
submit_button = (489, 661)
submit_button_color = (72, 137, 241)
submit_another_link = (760, 224)

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
             {'name': 'bob', 'fear': 'bees', 'source': 'amulet','robocop': 4, 'comments': 'n/a'},
             {'name': 'carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'please take the puppets out of the break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
             ]

pyautogui.PAUSE = 0.5

for person in form_data:
    # ユーザがスクリプトを中断する機会を与える
    print('>>>5秒間一時停止中。中断するにはctrl-cを押してください。<<<')
    time.sleep(5)

    # フォームページが読み込まれるのを待つ
    while not pyautogui.pixelMatchesColor(submit_button[0], submit_button[1], submit_button_color): #
        time.sleep(0.5)

    print('{}の情報を入力中...'.format(person['name']))    #
    pyautogui.click(name_field[0], name_field[1])   #

    # Name欄を入力する
    pyautogui.typewrite(person['name'] + '\t')  #

    # Greatest Fear(s)欄を入力する
    pyautogui.typewrite(person['fear'] + '\t')  #

    # Source os Wizard Powers欄を選択する
    if person['source'] == 'wand':  #
        pyautogui.typewrite(['down', '\t']) #
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t']) #
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t']) #
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t']) #

    # RoboCop欄を選択する
    if person['robocop'] == 1:  #
        pyautogui.typewrite([' ', '\t']) #
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right','\t'])


    # Additional Comments欄を入力する
    pyautogui.typewrite(person['comments'] + '\t')

    # Submitをクリックする
    pyautogui.press('enter')

    # 次のページが読み込まれるのを待つ
    print('送信ボタンを押しました。')
    time.sleep(5)

    # Submit another responseリンクをクリックする
    pyautogui.click(submit_another_link[0], submit_another_link[1])
