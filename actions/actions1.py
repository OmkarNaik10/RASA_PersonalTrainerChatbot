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

def bmi(x,y):
    querystring = {"weight":x,"height":y}
    url ="https://mega-fitness-calculator1.p.rapidapi.com/bmi"
    headers = {"X-RapidAPI-Host": "mega-fitness-calculator1.p.rapidapi.com",
	"X-RapidAPI-Key": "0e9ea9299cmsh7181dc2853b9830p132c6fjsnadeb96451fc7"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # h= float(input("enter:"))
    # w= float(input("enter:"))
    # n= input("enter:")
    # payload = {

    # "height": h,
    # "weight": w,
    # "Name": n

    #     }
    #r = requests.request("GET", URL, json=payload)
    #r = requests.get(url = URL) 
    data = response.text
    res = json.loads(data) 
    #ui=input("enter state:")
    # l=''
    # flag=False
    # for i in data:
    #     l=l+i
    
    l= str(res['info']['bmi'])+' '+res['info']['health']+' '+res['info']['healthy_bmi_range']
    return l

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_bmi_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        h=tracker.get_slot('height')
        x=float(h)*100
        print(type(h))
        w=tracker.get_slot('weight')
        print(type(w))
        #p=tracker.latest_message['text']
        temp=bmi(w,str(x))
        dispatcher.utter_template("utter_bmiresult",tracker,temp=temp)

        return []



