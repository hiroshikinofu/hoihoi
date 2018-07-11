import pyautogui, time
time.sleep(5)   #
pyautogui.click()   # お絵描きアプリをクリックしてフォーカスする
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)    # 右へ移動
    distance = distance - 5 #
    pyautogui.dragRel(0, distance, duration=0.2)    # 下へ移動
    pyautogui.dragRel(-distance, 0, duration=0.2)   # 左へ移動    
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)   # 上へ移動
