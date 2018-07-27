from chalice import Chalice, Response

from chalicelib.ews import ews
from chalicelib.ics import ics
from chalicelib.dining import dining
from chalicelib.library import library
from chalicelib.athletic import athletic

app = Chalice(app_name='UIUC-API')


@app.route('/')
def index():
    return Response(body='Welcome to University of Illinois, Urbana-Champaign API',
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})
# EWS router
@app.route('/ews', methods=['GET'])
def get_ews_status():
    return ews.EWSStatus().get_labs()


# ICS router
@app.route('/ics', methods=['GET'])
def get_ics_status():
    return ics.ICSStatus().get_labs()

@app.route('/ics/{department}', methods=['GET'])
def get_ics_by_department(department):
    return ics.ICSStatus().get_labs_by_department(department)


# athletic router
@app.route('/sports/check', methods=['GET'])
def check_sports():
    return athletic.AthleticSchedule().get_last_update()

@app.route('/sports/list', methods=['GET'])
def get_sports_list():
    return athletic.AthleticSchedule().get_sports_list()

@app.route('/sports/{sport}', methods=['GET'])
def get_sport(sport):
    return athletic.AthleticSchedule().get_sport(sport)


# dining router
@app.route('/dining/{hall}', methods=['GET'])
def get_dining_today(hall):
    return dining.Dining().get_menu_today(hall)

@app.route('/dining/{hall}/{date_from}', methods=['GET'])
def get_dining_date(hall, date_from):
    return dining.Dining().get_menu_date(hall, date_from, date_from)

@app.route('/dining/{hall}/{date_from}/{date_to}', methods=['GET'])
def get_dining_date_range(hall, date_from, date_to):
    return dining.Dining().get_menu_date(hall, date_from, date_to)


# library router
@app.route('/library', methods=['GET'])
def get_all_library():
    return library.Library().get_all()

@app.route('/library/{library_id}/{y}/{m}/{d}', methods=['GET'])
def search_library(library_id, y, m, d):
    return library.Library().search(library_id, y, m, d)
