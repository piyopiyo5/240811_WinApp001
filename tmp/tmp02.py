
# Import ---------------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog
# import pyautogui
# from PIL import Image, ImageTk, ImageChops
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import BoundedSemaphore, Event

# Constant -------------------------------------------------------------------
ON = 1
OFF = 0

# GlobalVariable -------------------------------------------------------------
Counter = 0
ThreadStopFlag = 0

# InternalFunction -----------------------------------------------------------


# TkinterWindow --------------------------------------------------------------
def RunAppMainWindow():
    #Global
    global MainWindow, IntervalEntry, CounterLabel
    
    #Variable
    RowNumber = 0
    
    # Tkinterウィンドウの作成
    MainWindow = tk.Tk()
    MainWindow.title("WinApp001")
    
    # ウィジェットを配置
    RowNumber+=1
    IntervalEntry = tk.Entry(MainWindow, width=4)
    IntervalEntry.grid(row=RowNumber, padx=5, pady=5, sticky="w")
    
    RowNumber+=1
    CounterLabel = tk.Label(MainWindow, text=str(Counter), font=("Arial", 20))
    CounterLabel.grid(row=RowNumber, padx=5, pady=5, sticky="w")
    
    RowNumber+=1
    IncreaseButton = tk.Button(MainWindow, text="Increase", command=IncreaseCounter, font=("Arial", 20))
    IncreaseButton.grid(row=RowNumber, padx=5, pady=5, sticky="w")
    
    # 閉じるボタンのイベントを設定
    MainWindow.protocol("WM_DELETE_WINDOW", CallBackClose)
    
    # アプリの実行
    MainWindow.mainloop()
    
# ウィンドウが閉じられたときに呼ばれる関数
def CallBackClose():
    global ThreadStopFlag
    ThreadStopFlag = 1
    MainWindow.destroy()
    
# ボタンが押されたときに呼ばれる関数
def IncreaseCounter():
    global Counter
    try:
        Counter += int(IntervalEntry.get())
        CounterLabel.config(text=str(Counter))
    except:
        pass
    
# thread ---------------------------------------------------------------------
def PrintTime():
    IntervalTIme = 4
    Time1 = datetime.now()
    while not ThreadStopFlag:
        Time2 = datetime.now()
        Timediff = Time2 - Time1
        if Timediff.seconds > IntervalTIme:
            print("Time:{}".format(Time2.strftime("%y%m%d_%H%M%S")))
            Time1 = Time2
        else:
            time.sleep(0.2)
    
# Main -----------------------------------------------------------------------
if __name__ == "__main__": 
    now = datetime.now()
    print("Start Time : {}".format(now.strftime("%y%m%d_%H%M%S")))
    ThreadPool = ThreadPoolExecutor(max_workers=3) # スレッド数を指定してスレッドプールを作成
    ThreadPool.submit(PrintTime) # 定周期時刻表示スレッドを作成
    RunAppMainWindow() # tkinter起動
    ThreadPool.shutdown() # プール内のすべてのスレッドが終了するまで待つ
    print("All Thereads End")
    