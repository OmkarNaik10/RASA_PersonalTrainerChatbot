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

import requests 

def univ(state):
    URL = "http://universities.hipolabs.com/search?country=United+States"
    r = requests.get(url = URL) 
    data = r.json() 
    #ui=input("enter state:")
    l=[]
    flag=False
    for i in range(10):
        if(data[i]['country']==state):
            l.append(data[i]['name'])
            flag=True

    if not flag:
        #print("does not exist")
        return None
    return l

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_uniname_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        state=tracker.latest_message['text']
        temp=univ(state)
        dispatcher.utter_template("utter_uniname",tracker,temp=temp)

        return []



