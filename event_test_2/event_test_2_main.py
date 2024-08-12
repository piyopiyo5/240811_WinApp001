from event_test_2_bus import EventBus
from event_test_2_module_a import ModuleA
from event_test_2_module_b import ModuleB
import time
from concurrent.futures import ThreadPoolExecutor

if __name__ == "__main__":
    # イベントバスのインスタンスを作成
    event_bus = EventBus()

    # 各モジュールにイベントバスを渡して初期化
    module_a = ModuleA(event_bus)
    module_b = ModuleB(event_bus)

    # # ModuleAがイベントを発行
    # module_a.trigger_event(1)
    # time.sleep(5)
    # module_a.trigger_event(2)
    
    # スレッド作成
    ThreadPool = ThreadPoolExecutor(max_workers=3) # スレッド数を指定してスレッドプールを作成
    ThreadPool.submit(module_a.process_task) # スレッドを作成
    ThreadPool.submit(module_b.process_task) # スレッドを作成
    
    
    
