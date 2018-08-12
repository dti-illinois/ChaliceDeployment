from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import re

class DailyIlliniScraper():

    def __init__(self):
        self.base_url = 'http://dailyillini.com/'

    def get_recent_news(self):
        response = self._request('feed/')
        soup = BeautifulSoup(response, 'lxml')
        return self._parse_xml(soup)

    def _parse_xml(self, data):
        result = []
        count = 0
        for item in data.find_all('item'):
            news = {}
            title = item.title.string
            date = item.pubdate.string
            description = re.findall(r'<description>(.*?)\.\.', str(item.description), flags=0)[0] + '...'
            news['title'] = title
            news['date'] = date
            news['description'] = description
            count += 1
            if count == 5:
                break
            result.append(news)
        return result

    def _request(self, url):
        req = Request(self.base_url + url, None,
        {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        response = urlopen(req)
        return response
