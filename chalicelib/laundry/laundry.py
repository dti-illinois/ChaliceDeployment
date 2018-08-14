from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

from chalicelib.laundry import laundry_consts

class LaundryStatus():

	def __init__(self):
		self.url = 'http://classic.laundryview.com/lvs.php?s=1506'

	def get_laundry_status(self):
		return self._load_data()

	def get_laundry_by_building(self, building_id):
		data = self._load_data()
		for building in data:
			if laundry_consts.building_id2name[building_id] == building['building']:
				return building
		return None

	def get_laundry_by_building_machine(self, building_id, machine):
		data = self._load_data()
		for building in data:
			if laundry_consts.building_id2name[building_id] == building['building']:
				return building[machine]
		return None

	def _load_data(self):
		response = urlopen(self.url).read().decode('utf-8')
		return self._parse_data(response)

	def _parse_data(self, data):
		results = []
		soup = BeautifulSoup(data, 'html.parser')
		elements = soup.find("div",{"id" : "campus1"}).findAll("span", {"class" : "user-avail"})
		for key in laundry_consts.switcher.keys():
			building = laundry_consts.building_id2name[key]
			for index, item in enumerate(laundry_consts.switcher[key]):
				washer_num = int(re.findall(r"\d+", elements[item - 1].get_text())[0])
				dryer_num = int(re.findall(r"\d+", elements[item - 1].get_text())[1])
				results.append({'building' : building, 'room' : laundry_consts.building_room_matcher[key][index], 'washer' : washer_num, 'dryer' : dryer_num})
		return results
