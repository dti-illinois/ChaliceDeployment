from urllib.request import urlopen
import json


class Library():

    def __init__(self):
        self.url_all = "https://quest.library.illinois.edu/LibDirectory/Api/UnitsWithCalendars"
        self.url_search = "https://quest.library.illinois.edu/LibDirectory/Api/SearchCalendar/"

    def get_all(self):
        response_json = urlopen(self.url_all)
        try:
            response = json.load(response_json)
            return response
        except ValueError:
            return None

    def search_library(self, library_id, y, m, d):
        request_url = self.url_search + str(library_id) + "/" + y + "/" + m + "/" + d
        response_json = urlopen(request_url)
        try:
            response = json.load(response_json)
            return response
        except ValueError:
            return None