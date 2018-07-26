from urllib.request import urlopen
import json

class ICSStatus():

    def __init__(self):
        self.url = 'https://www.ics.illinois.edu/e107/e107_plugins/ics_usage/api.php?_call=ICSUsage::getCurrent&department_name=ICS,HOUSING,UNION-IT'

    def get_labs(self):
        return self._load_data()['results']

    def get_labs_by_department(self, department):
        data = self._load_data()['results']
        return list(filter(lambda x: x['department_name']==department, data))

    def _load_data(self):
        response = urlopen(self.url)
        return json.load(response)
