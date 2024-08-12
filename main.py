
# Import ---------------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog
import pyautogui
# from PIL import Image, ImageTk, ImageChops
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import BoundedSemaphore, Event
import ctypes
from numLockKeeper import keepNumLock, stopNumlockKeeper, startNumlockKeep, endNumlockKeep
import queue

# Constant -------------------------------------------------------------------
ON = 1
OFF = 0

# GlobalVariable -------------------------------------------------------------
Counter = 0
ThreadStopFlag = 0


# InternalFunction -----------------------------------------------------------    
def CallBackClose():
    global ThreadStopFlag
    ThreadStopFlag = ON
    stopNumlockKeeper()
    MainWindow.destroy()
    
def ChangeStateOn():
    CounterLabel.config(text="State:ON")
    
def ChangeStateOff():
    CounterLabel.config(text="State:OFF")
    
CommandFunction=[ChangeStateOn, ChangeStateOff]
 
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
            
def RecieveCommand():
    while not ThreadStopFlag:
        command_event.wait()
        command_event.clear()
        CommandCount = command_queue.qsize()
        for i in range(CommandCount):
            CommandFunction[command_queue.get()]()
            
# TkinterWindow --------------------------------------------------------------
def RunAppMainWindow():
    #Global
    global MainWindow, CounterLabel
    
    #Variable
    RowNumber = 0
    
    # Tkinterウィンドウの作成
    MainWindow = tk.Tk()
    MainWindow.title("WinApp001")
    
    # ウィジェットを配置
    RowNumber+=1
    CounterLabel = tk.Label(MainWindow, text="NumLockKeeper", font=("Arial", 20))
    CounterLabel.grid(row=RowNumber, padx=5, pady=5, sticky="w")
    
    RowNumber+=1
    IncreaseButton = tk.Button(MainWindow, text="ON", command=startNumlockKeep, font=("Arial", 20))
    IncreaseButton.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
    
    IncreaseButton = tk.Button(MainWindow, text="OFF", command=endNumlockKeep, font=("Arial", 20))
    IncreaseButton.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
    
    CounterLabel = tk.Label(MainWindow, text="State:OFF", font=("Arial", 20))
    CounterLabel.grid(row=RowNumber, column=5, padx=5, pady=5, sticky="w")

    
    # 閉じるボタンのイベントを設定
    MainWindow.protocol("WM_DELETE_WINDOW", CallBackClose)
    
    # アプリの実行
    MainWindow.mainloop()
        
    
# Main -----------------------------------------------------------------------
if __name__ == "__main__": 
    now = datetime.now()
    print("Start Time : {}".format(now.strftime("%y%m%d_%H%M%S")))
    
    
    # コマンド用のイベントとキューを作成
    command_event = Event()
    command_queue = queue.Queue()
    
    # スレッド作成
    ThreadPool = ThreadPoolExecutor(max_workers=3) # スレッド数を指定してスレッドプールを作成
    ThreadPool.submit(PrintTime) # 定周期時刻表示スレッドを作成
    ThreadPool.submit(keepNumLock) # NumLockスレッドを作成
    ThreadPool.submit(RecieveCommand) # コマンド受信スレッドを作成
    
    RunAppMainWindow() # tkinter起動
    ThreadPool.shutdown() # プール内のすべてのスレッドが終了するまで待つ
    print("All Thereads End")
    
# ExternalFUnction
def sendCommandToMain(CommandID):
    command_queue.put(CommandID)
    command_event.set()