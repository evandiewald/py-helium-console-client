class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


class Device(Dict2Class):
    def __init__(self, device_dict):
        super().__init__(device_dict)


class Event(Dict2Class):
    def __init__(self, event_dict):
        super().__init__(event_dict)


class IntegrationEvent(Dict2Class):
    def __init__(self, event_dict):
        super().__init__(event_dict)


class Label(Dict2Class):
    def __init__(self, label_dict):
        super().__init__(label_dict)