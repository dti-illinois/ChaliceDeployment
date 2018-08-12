import json

class BuildingInfo():

    def __init__(self):
        self.path = 'chalicelib/building/data/buildings.json'
        with open(self.path, 'r') as f:
            self.data = json.load(f)

    def get_all_buildings(self):
        return self.data

    def search_by_building_num(self, num):
        for building in self.data:
            for sub_building in building:
                if int(sub_building['BLDG_NUM']) == num:
                    return building
        return 'no such building'
