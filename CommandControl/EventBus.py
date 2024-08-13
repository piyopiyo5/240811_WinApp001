# Class ----------------------------------------------------------------------
class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def publish(self, event_type, source, data=None):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(source, data)
        
# ExternalFunction -----------------------------------------------------------
# イベント発行
#   引数
#       EventBus: 使用するイベントバス。
#       EventType: 発行するイベントの名前。文字列。
#       Resorce: 発行元ID。
#       Data:イベントに付与するデータ。省略可能。
def publishEvent(EventBus, EventType, Resorce, Data=None):
    EventBus.publish(EventType, Resorce, Data)        
