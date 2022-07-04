import requests
import time
from tkinter import *
from selenium import webdriver
import os

url = "https://www.euro.com.pl/nawilzacze/smartmi-evaporative-humidifier.bhtml"

x = 2000

y_first = x

y= x

start = time.time()

myman = x

def openNewWindow():
    driver = webdriver.Chrome(executable_path="\chromedriver.exe")
    driver.maximize_window()
    driver.get(url)

def masterwindow():
    master = Tk()
    master.geometry("500x150")
    master.title("Spadek ceny laptopa")
    label = Label(master, text = myman + "PLN")
    label.config(font=("Courier", 44))
    label.pack(pady = 10)
    btn = Button(master, text ="KUP LAPTOPA NO SCAM FREE", command = openNewWindow)
    btn.pack(pady = 10)

def showcurrentTime():
    done = time.time()
    elapsed = done - start
    g = round(elapsed, 0)
    m = g//60%60
    s = g%60
    h = g//3600
    
    if s > 1 or s == 0:
        second = "s"
    else:
        second = ""
    if m > 1 or m == 0:
       minute = "s"
    else:
        minute = ""
    if h > 1 or h == 0:
        hour = "s"
    else:
        hour = ""
    print("Script has been running for:", h, "hour" + hour, m, "minute" + minute, s, "second" + second)

def timepass():
    t = 0
    while t < 300:
        time.sleep(1)
        t = t+1
        clearConsole()
        print("aktualna cena:", myman + "PLN")
        if y > x or x < y_first:
            #openNewWindow()
            masterwindow()
            mainloop()
        else:
            print("**** *****")
        showcurrentTime()
    t = 0


clearConsole = lambda: os.system('cls')
#input url
#url = input()
while True:

    r = requests.get(url).text
    cena = r.find("price")

    myman = r[ cena + 9 : cena + 12 ]

    clearConsole()

    print("aktualna cena:", myman + "PLN")

    myman.replace(".","")
    x = int(myman)

    #y_first=x

    if y > x or x < y_first:
        #openNewWindow()
        masterwindow()
        mainloop()
    else:
        print("**** *****")
        
    y = int(myman)
        #save y in a file
    timepass()

loop()