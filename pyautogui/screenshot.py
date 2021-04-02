import pyautogui
import datetime
import os
x=pyautogui.screenshot()
now = datetime.datetime.now()
y=now.strftime("%Y_%m_%dtime%H_%M_%S")+".png"
try:
    os.mkdir(y.split("time")[0])
except:
    pass
y=y.split("time")[0]+"/"+y.split("time")[1]
x.save(y)
