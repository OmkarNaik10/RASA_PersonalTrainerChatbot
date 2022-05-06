

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from sre_parse import State
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#import sys
#sys.path.append('C:\Omkar\SJSU_Notes\AI&DataEngineering\ChatBot\actions')
#from fake_abc_api import demograph
from rasa_sdk.events import SlotSet
import requests
import json 

import sqlite3

def datastore(exercise, details):
    conn=sqlite3.connect('gym.db')
    mycursor = conn.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS OmiGym (Exercise TEXT, Exercise_Details TEXT);""")
    mycursor.execute("INSERT INTO OmiGym VALUES (?,?)",(exercise,details))
    conn.commit()
    print(mycursor.rowcount,"record inserted")



# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_store"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         print('hello')    
#         x=tracker.get_slot('pushpull')
#         print(x)
#         y=tracker.get_slot('description')
#         print(y)
#         DataUpdate(tracker.get_slot('muscles'), tracker.get_slot('height'))
#         dispatcher.utter_message("Database Updated")
#         return []




class Actiondatabase(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        x=tracker.get_slot('pushpull')
        print("hello2")
        y=tracker.get_slot('description')
        datastore(x,y)
        dispatcher.utter_message("Database Updated")

        return []

#print("hello")