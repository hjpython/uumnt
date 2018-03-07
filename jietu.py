# encoding: UTF-8
import webbrowser,time
import pyautogui
pyautogui.FAILSAFE = True

j = 0
for i in range(234, 261):
    url = 'https://www.uumnt.cc/meinv/list_' + str(i) + '.html'
    webbrowser.open(url)
    while True:
        if len(list(pyautogui.locateAllOnScreen('webtitle.png'))) == j+1:
            x, y = pyautogui.locateCenterOnScreen('uumnt.png')
            pyautogui.moveTo(x,y)
            pyautogui.rightClick()
            pyautogui.moveTo(None, y + 313)
            pyautogui.moveTo(x + 390, None, 0.5)
            pyautogui.click()
            time.sleep(2)
            break
        else:
            time.sleep(0.3)
    j += 1
    if j == 30:
        time.sleep(16)
        x, y = pyautogui.locateCenterOnScreen('webclosed.png')
        pyautogui.click(x, y)
        pyautogui.moveTo(600, 600)
        j = 0
time.sleep(16)
x, y = pyautogui.locateCenterOnScreen('webclosed.png')
pyautogui.click(x, y)