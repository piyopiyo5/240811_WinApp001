# main.py

from event_test_bus import EventBus
from module_a import ModuleA
from module_b import ModuleB

if __name__ == "__main__":
    # イベントバスのインスタンスを作成
    event_bus = EventBus()

    # ModuleAとModuleBを初期化し、同じイベントバスを共有
    module_a = ModuleA(event_bus)
    module_b = ModuleB(event_bus)

    # 初期トリガー: ModuleAがModuleBにイベントを発行
    module_a.trigger_event_to_b()
