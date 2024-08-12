from event_test_2_bus import EventBus
import time

class ModuleA:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def trigger_event(self, eventid):
        print("Module A: Event triggered!")
        if eventid == 1:
            self.event_bus.publish("custom_event", 1, "Data from A")
        elif eventid == 2:
            self.event_bus.publish("custom_event2", 1, "Data from A")
            
    def process_task(self, task_id=None):
        while True:
            self.trigger_event(1)
            time.sleep(4)
            self.trigger_event(2)
            time.sleep(4)
            
