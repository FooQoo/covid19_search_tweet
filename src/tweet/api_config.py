import json


class ApiConfig:
    def __init__(self, filename):
        with open(filename) as f:
            self.keys = json.load(f)

        self.slot = 0

    def get_key(self):
        ck = self.keys['oauth2'][self.slot]['CONSUMER_KEY']
        cs = self.keys['oauth2'][self.slot]['CONSUMER_SECRET']
        at = self.keys['oauth2'][self.slot]['ACCESS_TOKEN']
        ats = self.keys['oauth2'][self.slot]['ACCESS_TOKEN_SECRET']

        if self.slot == len(self.keys)-1:
            self.slot = 0
        else:
            self.slot += 1

        return {
            'CONSUMER_KEY': ck,
            'CONSUMER_SECRET': cs,
            'ACCESS_TOKEN': at,
            'ACCESS_TOKEN_SECRET': ats
        }
