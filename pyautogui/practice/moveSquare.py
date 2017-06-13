import pyautogui

#停顿时间 1s
pyautogui.PAUSE = 1
#开启
pyautogui.FAILSAFE = True

for i in range (10) :
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration = 0.25)
    pyautogui.moveTo(100, 200, duration = 0.25)

    
