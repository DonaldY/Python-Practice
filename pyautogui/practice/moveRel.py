import pyautogui

#停顿时间 1s
pyautogui.PAUSE = 1
#开启
pyautogui.FAILSAFE = True

for i in range (10) :
    pyautogui.moveRel(100, 0, duration = 0.25)
    pyautogui.moveRel(0, 100, duration = 0.25)
    pyautogui.moveRel(-100, 0, duration = 0.25)
    pyautogui.moveRel(0, -100, duration = 0.25)

    
