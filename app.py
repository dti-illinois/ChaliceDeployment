from chalice import Chalice
from chalicelib.ews import ews

app = Chalice(app_name='UIUC-API')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/ews')
def get_all_ews_status():
    return ews.EWSStatus().get_all_labs()
