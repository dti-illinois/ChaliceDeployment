from urllib.request import urlopen
import json

class EWSStatus():

    def __init__(self):
        self.url = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'

    def get_all_labs(self):
        return self._load_data()

    def get_lab(self):
        pass

    def _load_data(self):
        response = urlopen(self.url)
        return json.load(response)


t = EWSStatus()
print(t.get_all_labs())
