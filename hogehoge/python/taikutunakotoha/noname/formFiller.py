
#! python3
# formFiller.py - フォームの自動入力

import pyautogui, time
# pyautoguiモジュールとtimeモジュールをインポートしろ
# 補足「pyautoguiモジュール」は、キーボード入力、マウス移動、ボタンクリック、
# マウスのホイール操作をシミュレートする関数がある

# 補足「timeモジュール」は、コンピュータのシステムクロックは、特定の日付や時刻、
# タイムゾーンが設定されている。組み込みのtimeモジュールを使えば、
# Pythonプログラムからシステムクロックを読み出して現在時刻を取得することが可能

# 以下の値は実際に調べたものに置き換えること。
name_field = (565, 338)                 #1
submit_button = (489, 661)              #2
submit_button_color = (72, 137, 241)    #3
submit_another_link = (629, 262)

#1 ブラウザ全画面時のName欄のx.y座標
#2 ブラウザ全画面時の送信ボタンのx.y座標
#3 送信ボタンのRGB値のタプル

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
             {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
             {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'please take the puppets out of the break room.'},
             {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
             ]          # 辞書データを変数「form_data」に入れろ

pyautogui.PAUSE = 0.5       #4

for person in form_data:                                             #5
    # ユーザがスクリプトを中断する機会を与える
    print('>>> 5秒間一時停止中。中断するにはctrl-cを押してください。<<<') #6
    time.sleep(5)                                                    #7

#4 各関数を呼び出した後に0.5秒待て
#5 変数「from_data」の要素を、変数parsonに順次入れる間、以下の処理を繰り返せ
#6 「>>>5秒間一時停止中。中断するにはctrl-cを押してください。<<<」を表示しろ
#7 pythonプログラムを5秒間停止しろ

    # フォームページが読み込まれるのを待つ
    while not pyautogui.pixelMatchesColor(submit_button[0], submit_button[1], submit_button_color):     #8
        time.sleep(0.5)     #9

        print('{}の情報を入力中...'.format(person['name']))    #10
        pyautogui.click(name_field[0], name_field[1])         # 11

        # Name欄を入力する
        pyautogui.typewrite(person['name'] + '\t')            #12

        # Greatest Fear(s)欄を入力する
        pyautogui.typewrite(person['fear'] + '\t')            #13


#8 送信ボタンの座標と色が一致しなくなるまで、以下の処理を繰り返せ
#9 pythonプログラムを0.5秒間停止しろ
#10「'{}の情報を入力中...'.format(person['name'])」を表示しろ
#11 neme欄の座標をクリックしろ
#12 name欄に要素nameを入力し、その後「Tab」ボタンを入力、次の入力フォームを選択しろ
#13 Greatest Fear(s)欄に要素fearを入力し、その後「Tab」ボタンを入力、次の入力フォームを選択しろ

            # Source os Wizard Powers欄を選択する
        if person['source'] == 'wand':                                  #14
            pyautogui.typewrite(['space', 'down', '\t'])
        elif person['source'] == 'amulet':                              #15
            pyautogui.typewrite(['space', 'down', 'down', '\t'])
        elif person['source'] == 'crystal ball':                        #16
            pyautogui.typewrite(['space', 'down', 'down', 'down', '\t'])
        elif person['source'] == 'money':                               #17
            pyautogui.typewrite(['space', 'down', 'down', 'down', 'down', '\t'])

#14 もし変数parsonの要素「source」が、文字列downと等しい場合、
#14 Wizard Powers欄のプルダウンで下キーを1度タイプし、Tabキーを入力して
#14 次の入力フォームを選択しろ

#15 もし変数parsonの要素「source」が、文字列amuletと等しい場合、
#15 Wizard Powers欄のプルダウンで下キーを2度タイプし、Tabキーを入力して
#15 次の入力フォームを選択しろ

#16 もし変数parsonの要素「source」が、文字列crystal ballと等しい場合、
#16 Wizard Powers欄のプルダウンで下キーを3度タイプし、Tabキーを入力して
#16 次の入力フォームを選択しろ

#17 もし変数parsonの要素「source」が、文字列moneyと等しい場合、
#17 Wizard Powers欄のプルダウンで下キーを4度タイプし、Tabキーを入力して
#17 次の入力フォームを選択しろ

        # RoboCop欄を選択する
        if person['robocop'] == 1:                                          #18
            pyautogui.typewrite(['space', '\t'])
        elif person['robocop'] == 2:                                        #19
            pyautogui.typewrite(['space', 'right', '\t'])
        elif person['robocop'] == 3:                                        #20
            pyautogui.typewrite(['space', 'right', 'right', '\t'])
        elif person['robocop'] == 4:                                        #21
            pyautogui.typewrite(['space', 'right', 'right', 'right', '\t'])
        elif person['robocop'] == 5:                                        #22
            pyautogui.typewrite(['space', 'right', 'right', 'right', 'right','\t'])
#18 もし変数personの要素robocopが、数値1と等しい場合、
#18　RoboCop欄でスペースキーを1度入力後、tabキーを入力し、次の入力フォームを選択しろ

#19 もし変数personの要素robocopが、数値2と等しい場合、
#19　RoboCop欄で右方向キーを1度入力後、tabキーを入力し、次の入力フォームを選択しろ

#20 もし変数personの要素robocopが、数値3と等しい場合、
#20　RoboCop欄で右方向キーを2度入力後、tabキーを入力し、次の入力フォームを選択しろ

#21 もし変数personの要素robocopが、数値4と等しい場合、
#21　RoboCop欄で右方向キーを3度入力後、tabキーを入力し、次の入力フォームを選択しろ

#22 もし変数personの要素robocopが、数値5と等しい場合、
#22　RoboCop欄で右方向キーを4度入力後、tabキーを入力し、次の入力フォームを選択しろ


        # Additional Comments欄を入力する
        pyautogui.typewrite(person['comments'] + '\t')                      #23

        # Submitをクリックする
        pyautogui.press('enter')                                            #24

        # 次のページが読み込まれるのを待つ
        print('送信ボタンを押しました。')                                     #25
        time.sleep(5)

        # Submit another responseリンクをクリックする
        pyautogui.click(submit_another_link[0], submit_another_link[1])     #26

#23 変数personの要素commentsをAdditional Comments欄に入力し、tabキーを入力しろ
#24 Enterキーを入力しろ
#25 「送信ボタンを押しました。」を表示し、プログラムを5秒間停止しろ
#26 Submit another responseリンクをクリックしろ
