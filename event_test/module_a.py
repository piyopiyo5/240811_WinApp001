# module_a.py

from event_test_bus import EventBus
import time

class ModuleA:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe("event_from_b", self.handle_event_from_b)

    def trigger_event_to_b(self):
        print("Module A: Event triggered for B!")
        self.event_bus.publish("event_from_a", "Data from A")

    def handle_event_from_b(self, data):
        print(f"Module A: Event received from B with data: {data}")
        # Bからのイベントに反応して、再度Bに通知する例
        time.sleep(1)
        self.trigger_event_to_b()
