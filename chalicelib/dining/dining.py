from urllib.request import urlopen
import json

class Dining():

    def __init__(self):
        self.url = 'https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04'

    def get_menu_today(self, hall):
        request_url = self.url + "&id=" + hall + "&t=json"
        response = urlopen(request_url)
        try:
            return json.load(response)
        except:
            return ''

    def get_menu_date(self, hall, date_from, date_to):
        request_url = self.url + "&id=" + hall + "&from=" + date_from +"&to=" + date_to + "&t=json"
        response = urlopen(request_url)
        try:
            return json.load(response)
        except:
            return ''
