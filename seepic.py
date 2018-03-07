# coding:utf-8
import pyHook
import pythoncom
import time
import pyautogui
import win32api

def onKeyboardEvent(event):
    #print("Key:", event.Key)
    if event.Key == '3':
        pyautogui.dragRel(155, None, button='left')
        time.sleep(0.1)
        pyautogui.hotkey('ctrlleft', 'c')
        win32api.ShellExecute(0, 'open', r'D:\software\an\everything\Everything.exe', '', '', 1)
        time.sleep(0.5)
        pyautogui.hotkey('ctrlleft', 'v')
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press(['right', 'left'])
        pyautogui.press('enter')
    elif event.Key == 'Space':
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click()
        pyautogui.press('esc')
        time.sleep(0.2)
        try:
            x, y = pyautogui.locateCenterOnScreen('fileclosed.png')
        except:
            x, y = pyautogui.locateCenterOnScreen('fileclosedwhite.png')
        pyautogui.click(x, y)
        pyautogui.moveTo(currentMouseX, currentMouseY)
    return True

def main():
    # 创建一个：'钩子'管理对象
    hm = pyHook.HookManager()
    # 监听所有的键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘'钩子'
    hm.HookKeyboard()
    # 进入循环侦听，需要手动进行关闭，否则程序将一直处于监听的状态。可以直接设置而空而使用默认值
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()

