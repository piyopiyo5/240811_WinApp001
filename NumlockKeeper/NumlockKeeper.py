# Import ---------------------------------------------------------------------
import time
from concurrent.futures import ThreadPoolExecutor
from CommandControl.EventBus import EventBus, publishEvent
from threading import Event
import pyautogui
import ctypes

# Constant -------------------------------------------------------------------
ON = 1
OFF = 0
NUMLOCK_KEEPER = 1 # モジュールID

# GlobalVariable -------------------------------------------------------------
NumLockKeepState = OFF
ThreadStopRequest = OFF
NumLockKeepStopRequest = OFF

# EventFlag ----------------------------------------------------------------------
NumLockKeepStartEvent = Event()

# InternalFunction -----------------------------------------------------------   
# Numlockの有効状態確認
def IsNumlockOn():
    # GetKeyState(0x90) でNumLockキーの状態を確認する
    return ctypes.windll.user32.GetKeyState(0x90) & 0x0001 != 0

# NumLockキーを切り替え
def ToggleNumlock():
    pyautogui.press('numlock')
    
# NumlockKeeper開始
def StartNumlockKeeper(source, data):
    if NumLockKeepState == OFF:
        NumLockKeepStartEvent.set()
        pass

# NumlockKeeper停止
def StopNumlockKeeper(source, data):
    global NumLockKeepStopRequest
    if NumLockKeepState == ON:
        NumLockKeepStopRequest = ON
        
# NumlockKeeper状態更新
def updateNumlockKeeperState(State):
    global NumLockKeepState, SharedEventBus
    NumLockKeepState = State
    if State == ON:
        publishEvent(SharedEventBus, "LabelUpdateRequest", NUMLOCK_KEEPER, {"NumLockKeeperStateLabel":"State:ON"})
    else:
        publishEvent(SharedEventBus, "LabelUpdateRequest", NUMLOCK_KEEPER, {"NumLockKeeperStateLabel":"State:OFF"})
        
# NumlockKeeperのスレッド関数 
def KeepNumlockOn():
    global NumLockKeepStopRequest
    while not ThreadStopRequest:
        EventSet = NumLockKeepStartEvent.wait(timeout=2)
        if not EventSet:
            continue
        NumLockKeepStartEvent.clear()
        updateNumlockKeeperState(ON)
        while True:
            if NumLockKeepStopRequest:
                NumLockKeepStopRequest = OFF
                updateNumlockKeeperState(OFF)
                break
            else:
                if not IsNumlockOn():
                    ToggleNumlock()
            if ThreadStopRequest:
                break
            time.sleep(1)

# ExternalFunction -----------------------------------------------------------
# NumlockKeeperの初期化処理
def initNumlockKeeper(EventBus):
    # global
    global SharedEventBus
    
    # イベントバス取得
    SharedEventBus = EventBus
    
    # イベントのサブスクライブ
    SharedEventBus.subscribe("NumlockKeeperStartRequest", StartNumlockKeeper)
    SharedEventBus.subscribe("NumlockKeeperStopRequest", StopNumlockKeeper)
    
    # スレッド作成
    ThreadPool = ThreadPoolExecutor(max_workers=3) # スレッド数を指定してスレッドプールを作成
    ThreadPool.submit(KeepNumlockOn) # NumlockKeeperスレッドを作成
    
# NumlockKeeperの終了処理
def endNumlockKeeper():
    global ThreadStopRequest
    ThreadStopRequest = ON
