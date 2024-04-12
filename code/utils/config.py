import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
while os.path.basename(root_dir) != 'NearestPointOfInterest':
    root_dir = os.path.dirname(root_dir)


PGPASS = '100Could!'
GMAPS_KEY = None
DBNAME = 'ChiTownInnovate'
USERNAME = 'coltonlapp'
HOST = 'localhost'
LOGO_DIR = os.path.join(root_dir, 'code', 'img', 'logos')
GMAPS_API_KEY = 'AIzaSyDBoyZCkbAwxjwA_j_dIOUMVCAmOvFGshY'