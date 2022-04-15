from flask import render_template, request
from app import app
from models.event_list import add_new_event, events
from models.event import Event


@app.route('/')
def index():
    return 'homepage'

@app.route('/events')
def events_list():
    return render_template('index.html', title='Home', events = events)


@app.route('/events', methods=['POST'])
def add_event():
    eventDate = request.form['date']
    eventName = request.form['name']
    eventGuests = request.form['number_of_guests']
    eventRoom = request.form['room_location']
    eventDesc = request.form['description']

    if 'recurring' in request.form:
        eventRecc = True
    else:
        eventRecc = False

    newEvent = Event(input_date=eventDate,
                     input_name_of_event=eventName, input_number_of_guests=eventGuests, input_room_location=eventRoom, input_description=eventDesc, input_recurring=eventRecc)
    
    add_new_event(newEvent)

    return render_template('index.html', title='Home', events=events)

# @app.route('.events/delete/<name', methods =['POST'])