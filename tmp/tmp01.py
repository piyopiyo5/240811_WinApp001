# マルチスレッドとセマフォとイベントフラグの使い方を確認

# Import
from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime
from threading import BoundedSemaphore, Event

# Constant
MAX_CONCURRENT_TASKS = 3

# EventFlag
timeCheckEvent = Event()

# Thread
def printStr(ID, Str, interval, cycle):
    sem.acquire()
    for i in range(cycle):
        print("ID:{}, Str:{}, Time:{}".format(ID, Str, i*interval))
        time.sleep(interval)
    sem.release()
    
def printTime():
    now = datetime.now()
    print("Wait Start  Time:{}".format(now.strftime("%y%m%d %H%M%S")))
    timeCheckEvent.wait()
    now = datetime.now()
    print("Event Get!  Time:{}".format(now.strftime("%y%m%d %H%M%S")))
      
# Main
if __name__ == "__main__": 
    
    print("Start!")
    
    sem = BoundedSemaphore(value=MAX_CONCURRENT_TASKS) # リソース数上限ありのセマフォを作成
    executor1 = ThreadPoolExecutor(max_workers=5) # スレッドのインスタンス（プール）を作成。この時にプール内のスレッド数上限を設定できる。

    for i in range(3):
        executor1.submit(printStr, i, "AAA", 2, 2) # submitでスレッドAを生成
        executor1.submit(printStr, i, "BBB", 3, 2) # submitでスレッドBを生成

    executor1.shutdown() # プール内のすべてのスレッドが終了するまで待つ
    
    print("===========================")
    
    executor2 = ThreadPoolExecutor(max_workers=3) # スレッドのインスタンスを作成
    
    executor2.submit(printTime) # submitでスレッドを生成
    time.sleep(5)
    timeCheckEvent.set()
    
    executor2.shutdown() # プール内のすべてのスレッドが終了するまで待つ

    print("End!")