import json

class Instrument:
    def __init__(self, dict):
        self.instrument = dict.get("instrument")
        self.user = dict.get("user")

    def create_json(self):
        return json.dumps(self.__dict__)

test = Instrument()


