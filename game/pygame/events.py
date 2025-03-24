class Events:
    def __init__(self):
        self.events = []

    def add(self, event):
        self.events.append(event)

    def get(self):
        return self.events

    def clear(self):
        self.events = []