# Import -------------------------------------------------------------------
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from CommandControl.EventBus import EventBus, publishEvent
from NumlockKeeper.NumlockKeeper import initNumlockKeeper, endNumlockKeeper

# Constant -------------------------------------------------------------------
DEBUG_MODE = 1
ON = 1
OFF = 0
MAIN_MODEULE = 0 # モジュールID

# GlobalVariable -------------------------------------------------------------
Counter = 0
ThreadStopFlag = OFF

# InternalFunction -----------------------------------------------------------    
# Tkinterウィンドウを閉じたときのコールバック関数
def CallBackClose():
    global ThreadStopFlag
    # main.py内のスレッドの終了処理フラグ
    ThreadStopFlag = ON
    # 各モジュールの終了処理
    endNumlockKeeper()
    #tkinterウィンドウの終了処理
    MainWindow.destroy()

# Tkinterウィンドウの実行関数
def RunAppMainWindow():
    # Global
    global MainWindow, NumLockKeeperStateLabel
    
    #Variable
    RowNumber = 0
    
    # Tkinterウィンドウの作成
    MainWindow = tk.Tk()
    MainWindow.title("WinApp001")
    
    # ウィジェットを配置
    RowNumber+=1
    CounterLabel = tk.Label(MainWindow, text="NumLockKeeper", font=("Arial", 20))
    CounterLabel.grid(row=RowNumber, column=1, padx=5, pady=5, sticky="w")
    
    RowNumber+=1
    OnButton = tk.Button(MainWindow, text="ON", command=lambda: publishEvent(SharedEventBus, "NumlockKeeperStartRequest", MAIN_MODEULE), font=("Arial", 20))
    OnButton.grid(row=RowNumber, column=2, padx=5, pady=5, sticky="w")
    
    OffButton = tk.Button(MainWindow, text="OFF", command=lambda: publishEvent(SharedEventBus, "NumlockKeeperStopRequest", MAIN_MODEULE), font=("Arial", 20))
    OffButton.grid(row=RowNumber, column=3, padx=5, pady=5, sticky="w")
    
    RowNumber+=1
    NumLockKeeperStateLabel = tk.Label(MainWindow, text="State:OFF", font=("Arial", 20))
    NumLockKeeperStateLabel.grid(row=RowNumber, column=2, columnspan=2, padx=5, pady=5, sticky="w")
    
    # 閉じるボタンのイベントを設定
    MainWindow.protocol("WM_DELETE_WINDOW", CallBackClose)
    
    # アプリの実行
    MainWindow.mainloop()
    
# 定周期時刻printスレッド
def RepeatPrintTime():
    INTERVAL_TIME = 10
    while not ThreadStopFlag:
        for i in range(INTERVAL_TIME):
            if ThreadStopFlag:
                break
            time.sleep(1)
        now = datetime.now()
        res = print("Time : {}".format(now.strftime("%y%m%d_%H%M%S"))) if DEBUG_MODE else None
        
# ラベル表示更新
def UpdateLabelText(source, data):
    try:
        keys = data.keys()
        for key in keys:
            if key in globals():
                globals()[key].config(text=data[key])
    except:
        pass

# Main -----------------------------------------------------------------------
if __name__ == "__main__": 
    now = datetime.now()
    res = print("Start Time : {}".format(now.strftime("%y%m%d_%H%M%S"))) if DEBUG_MODE else None
    
    # イベントバス作成
    SharedEventBus = EventBus()
    
    # イベントのサブスクライブ
    SharedEventBus.subscribe("LabelUpdateRequest", UpdateLabelText)
    
    # スレッド作成
    ThreadPool = ThreadPoolExecutor(max_workers=3) # スレッド数を指定してスレッドプールを作成
    ThreadPool.submit(RepeatPrintTime) # 定周期時刻表示スレッドを作成
    
    # 各モジュールを初期化
    initNumlockKeeper(SharedEventBus)
    
    # tkinterウィンドウ表示
    RunAppMainWindow()