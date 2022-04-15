from models.event import *

event1 = Event("13/04/2022","Homework","22","Zoom","Weekend Homework", True)
event2 = Event("14/04/2022","Boozy Night","22","The Chanter","Bottoms Up", False)

events = [event1,event2]


def add_new_event(event):
    events.append(event)
