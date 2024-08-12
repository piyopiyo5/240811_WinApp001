# Import ---------------------------------------------------------------------
import time
from threading import Event
import ctypes
import pyautogui
from main import sendCommandToMain

# Constant -------------------------------------------------------------------
ON = 1
OFF = 0

# GlobalVariable -------------------------------------------------------------
ThreadStopFlag = OFF

# Event
NumLockKeepStartEvent = Event()

# Flag
NumLockKeepEndFlag = OFF
NumLockKeepState = OFF

# InternalFunction -----------------------------------------------------------
def IsNumlockOn():
    """NumLockが有効かどうかを確認する"""
    # GetKeyState(0x90) でNumLockキーの状態を確認する
    return ctypes.windll.user32.GetKeyState(0x90) & 0x0001 != 0

def ToggleNumlock():
    """NumLockキーを切り替える"""
    pyautogui.press('numlock')
    

# ExternalFunction -----------------------------------------------------------
def keepNumLock():
    global NumLockKeepEndFlag, NumLockKeepState
    while not ThreadStopFlag:
        EventSet = NumLockKeepStartEvent.wait(timeout=2)
        if not EventSet:
            continue
        NumLockKeepStartEvent.clear()
        NumLockKeepState = ON
        sendCommandToMain(0)
        while True:
            if NumLockKeepEndFlag:
                NumLockKeepEndFlag = OFF
                NumLockKeepState = OFF
                sendCommandToMain(1)
                break
            else:
                if not IsNumlockOn():
                    ToggleNumlock()
            if ThreadStopFlag:
                break
            time.sleep(1)
            
# スレッド停止
def stopNumlockKeeper():
    global ThreadStopFlag
    ThreadStopFlag = ON
    
# NumlockKeep有効化
def startNumlockKeep():
    if not NumLockKeepState:
        NumLockKeepStartEvent.set()

# NumlockKeep無効化
def endNumlockKeep():
    global NumLockKeepEndFlag
    if NumLockKeepState:
        NumLockKeepEndFlag = ON