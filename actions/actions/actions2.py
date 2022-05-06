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
import json 

# def bmi(h,w,n):
#     URL ="http://localhost:3001/api/getBMI"
#     # h= float(input("enter:"))
#     # w= float(input("enter:"))
#     # n= input("enter:")
#     payload = {

#     "height": h,
#     "weight": w,
#     "Name": n

#         }
#     r = requests.request("GET", URL, json=payload)
#     #r = requests.get(url = URL) 
#     data = r.text
#     res = json.loads(data) 
#     #ui=input("enter state:")
#     # l=''
#     # flag=False
#     # for i in data:
#     #     l=l+i

#     return res['message']

def calories(x):
    url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

    querystring = {"ingr":x}
    headers = {"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
    "X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data=response.text
    res = json.loads(data)

    return res['calories'] 

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_calories_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        p=tracker.latest_message['text']
        temp=calories(p)
        temp=str(temp)+'  calories'
        dispatcher.utter_template("utter_caloriesresult",tracker,temp=temp)

        return []



