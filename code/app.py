from flask import Flask, render_template, request
from main import create_map  # Ensure this is the correct import for your create_map function
import time

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    """Display the initial page with the 'Generate Map' button."""
    # read in html at templates/map.html
    

    if request.method == 'POST':

        out = create_map()
        my_map = out['map']

        # Read in the HTML from the map.html file
        with open('templates/map.html', 'r') as file:
            map_html = file.read()

        # unpack other variables from out dictionary
        random_time = out['random_time']
        random_date = out['random_date']
        random_coords = out['random_coords']
        closest_event_location = out['closest_event_location']
        closest_event_name = out['closest_event_name']
        closest_event_desc = out['closest_event_desc']
        closest_event_time = out['closest_event_time']
        closest_event_date = out['closest_event_date']
        closest_event = out['closest_event']
        directions_result = out['directions_result']
        directions_html = out['directions_html']

    elif request.method == 'GET':
        map_html = None
        random_time = None
        random_date = None
        random_coords = None
        closest_event_location = None
        closest_event_name = None
        closest_event_desc = None
        closest_event_time = None
        closest_event = None
        directions_html = None
        closest_event_date = None
        
    timestamp = int(time.time())  # Get the current timestamp

    print(f"timestamp: {timestamp}")
    print(f"map_html: {map_html}")

    return render_template('index.html', map_html=map_html, timestamp=timestamp, random_time=random_time, random_date=random_date,
                           random_coords=random_coords,  closest_event_location=closest_event_location,
                           closest_event_name=closest_event_name,
                           closest_event_desc=closest_event_desc, closest_event_time=closest_event_time,
                           closest_event_date=closest_event_date,
                           closest_event=closest_event, directions_html=directions_html)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == "__main__":
    app.run(debug=True)
