# coding=utf-8
import webbrowser
import time

n = 1


print("程序启动于" + time.ctime())

while n < 4:
    time.sleep(10)
    webbrowser.open("www.163.com")
    s = str(n)
    print("第" + s + "次休息开始于" + time.ctime())
    n = n + 1
