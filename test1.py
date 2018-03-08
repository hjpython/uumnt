import pyHook
import pythoncom
import os,time
import pyautogui
import win32api

# pyautogui.hotkey('ctrlleft', 'c')
# win32api.ShellExecute(0, 'open', r'D:\software\an\everything\Everything.exe', '', '', 1)
# time.sleep(1)
# pyautogui.hotkey('ctrlleft', 'v')
# pyautogui.press('enter')
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.press(['right', 'left'])
# pyautogui.press('enter')
#
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# # pyautogui.click(1888, 13)
# # pyautogui.moveTo(currentMouseX, currentMouseY)

# def onKeyboardEvent(event):
#     print("Key:", event.Key)
#     if event.Key == 'Space':
#         pyautogui.click()
#         pyautogui.keyDown('shiftleft')
#         pyautogui.press(['right', 'right','right','right','right','right','right','right'])
#         pyautogui.keyUp('shift')
#         pyautogui.hotkey('ctrl', 'c')
#     return True
#
# def main():
#     # 创建一个：'钩子'管理对象
#     hm = pyHook.HookManager()
#     # 监听所有的键盘事件
#     hm.KeyDown = onKeyboardEvent
#     #设置键盘'钩子'
#     hm.HookKeyboard()
#     # 进入循环侦听，需要手动进行关闭，否则程序将一直处于监听的状态。可以直接设置而空而使用默认值
#     pythoncom.PumpMessages()
#
# if __name__ == "__main__":
#     main()

# pyautogui.click(229, 100)
# pyautogui.hotkey('shift', 'shift','right')
# # pyautogui.keyDown('shift')
# # pyautogui.press(['right', 'right','right','right','right','right','right','right',])
# # pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')

# pyautogui.prompt(text='', title='' , default='')
# pyautogui.screenshot('webclosedxiao.png', region=(1643,57,240,33))
# i = 0
# while True:
#     # pyautogui.screenshot('fileclosed'+str(i)+'.png', region=(1860, 0, 55, 25))
#     # i += 1
#     # time.sleep(1)
#     # print(i)
#     try:
#         x, y = pyautogui.locateCenterOnScreen('fileclosed.png')
#         print(x, y)
#     except:
#         x, y = pyautogui.locateCenterOnScreen('fileclosedwhite.png')
#         print(x, y)

# pyautogui.click(x, y)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(90,169)
# pyautogui.dragRel(170, None, 0.3, button='left')
#print(pyautogui.locateOnScreen(r'D:\(hp)google\pycharm\uumnt\url.png'))
# x, y = pyautogui.locateCenterOnScreen('uumnt.png', grayscale=True)
# pyautogui.rightClick()
# pyautogui.moveTo(None, y + 313)
# pyautogui.moveTo(x + 390, None, 0.5)
#pyautogui.moveTo(x + 361, y + 313, 1)
# d = {0:'hj',1:'lll'}
# print(d[1])

d = ['hj','lll']
print(d[1])