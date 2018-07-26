from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime
import json

#from chalicelib.athletic import athletic_consts
import athletic_consts

class AthleticScheduleScraper():

    def __init__(self):
        self.url = 'http://www.fightingillini.com/schedule.aspx?path='
        self.sports = list(athletic_consts.sports_dict.keys())
        self.path = 'data/sports.json'

    def print_to_file(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self._get_sports()
        json_text = {
        'last_update': now,
        'data': data
        }
        with open(self.path, 'w') as f:
            json.dump(json_text, f, indent=4)

    def _get_sports(self):
        data = {}
        for sport in self.sports:
            data[sport] = self._get_sport(sport)
        return data

    def _get_sport(self, sport):
        response = self._request(sport)
        sport_info = self._parse_html(response)
        return sport_info

    def _request(self, sport):
        request_url = self.url + sport
        req = Request(request_url, None,
        {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        response = urlopen(req)
        return response

    def _parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        games = []
        for item in soup.find_all(class_='schedule_game'):
            game = {}
            game['opponent'] = self._get_opponent(item)
            game['date'] = self._get_date(item)
            game['time'] = self._get_time(item)
            game['location'] = self._get_location(item)
            game['result'] = self._get_result(item)
            games.append(game)
        return games

    def _get_opponent(self, game):
        opponent_div = game.find(class_='schedule_game_opponent_name')
        if opponent_div.a is None and opponent_div.span is None:
            return opponent_div.string.strip()
        elif opponent_div.span is None:
            if opponent_div.a.string is None:
                return opponent_div.a.span.string.strip()
            else:
                return opponent_div.a.string.strip()
        else:
            return opponent_div.span.string.strip()

    def _get_date(self, game):
        date_div = game.find(class_='schedule_game_opponent_date')
        return date_div.string.strip()

    def _get_time(self, game):
        time_div = game.find(class_='schedule_game_opponent_time')
        return time_div.string.strip()

    def _get_location(self, game):
        location_div = game.find(class_='schedule_game_location')
        if location_div.span is None:
            return location_div.string.strip()
        else:
            if location_div.span.string is None:
                return 'not available'
            else:
                return location_div.span.string.strip()

    def _get_result(self, game):
        result_div = game.find(class_='schedule_game_results')
        if result_div is None or len(result_div.div.contents) == 0:
            return 'not available'
        else:
            return result_div.div.contents[0]

#t = AthleticScheduleScraper()
#t.print_to_file()
