from event_test_2_bus import EventBus
from threading import Event

class ModuleB:
    
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe("custom_event", self.handle_event)
        self.event_bus.subscribe("custom_event2", self.handle_event2)
        self.command_event = Event()
        self.command_list = []

    def handle_event(self, source, data):
        print(f"Module B: Event received with data: {data}")
        self.command_list.append([source,data])
        self.command_event.set()
        
    def handle_event2(self, source, data):
        print(f"Module B: Event2 received with data: {data}")
        self.command_list.append([source,data])
        self.command_event.set()
        
    def process_task(self, task_id=None):
        while True:
            self.command_event.wait()
            self.command_event.clear()
            print(self.command_list.pop())
            
            
