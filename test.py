import pyHook
import pythoncom
import os,time
import pyautogui
import win32api

#win32api.ShellExecute(0,'open',r'D:\software\an\everything\Everything.exe','','',1)
#win32api.ShellExecute(0,'open',r'D:\software\an\notepad\Notepad++\notepad++.exe','','',1)
#pyautogui.moveTo(50, 80, 1)
#pyautogui.click(70, 181)
# pyautogui.click(button='right')
#pyautogui.click(clicks=2, interval=0.25)

# time.sleep(1)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.press('right')
# pyautogui.press('left')
# pyautogui.press('enter')

#pyautogui.press('enter')
#pyautogui.typewrite('hello world')
# pyautogui.moveTo(1890,15)
def onKeyboardEvent(event):
    print("Key:", event.Key)
    if event.Key == 'Space':
        pyautogui.keyDown('ctrlleft')
        i = 0
        while i < 19:
            pyautogui.click()
            pyautogui.moveRel(None, 85, 0.1)
            i += 1
        pyautogui.keyUp('ctrlleft')
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

#
# print(currentMouseX, currentMouseY)
# pyautogui.click(59, 200, clicks=2)
# pyautogui.moveTo(currentMouseX, currentMouseY)