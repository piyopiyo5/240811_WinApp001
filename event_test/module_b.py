# module_b.py

from event_test_bus import EventBus

class ModuleB:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe("event_from_a", self.handle_event_from_a)

    def trigger_event_to_a(self):
        print("Module B: Event triggered for A!")
        self.event_bus.publish("event_from_b", "Data from B")

    def handle_event_from_a(self, data):
        print(f"Module B: Event received from A with data: {data}")
        # Aからのイベントに反応して、再度Aに通知する例
        self.trigger_event_to_a()
