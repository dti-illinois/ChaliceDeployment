import json

from chalicelib.athletic import athletic_consts

class AthleticSchedule():

    def __init__(self):
        self.path = 'chalicelib/athletic/data/sports.json'
        with open(self.path, 'r') as f:
            raw = json.load(f)
            self.last_update = raw['last_update']
            self.data = raw['data']

    def get_last_update(self):
        return {'last_update': self.last_update}

    def get_sports_list(self):
        return athletic_consts.sports_dict

    def get_sport(self, sport):
        return self.data[sport]

    def get_sports(self):
        return self.data
