# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather
import requests
from Brain import response_processor_brain
from FAQ import knowledge
#from pymongo import MongoClient
#
#
#client = MongoClient('mongodb://127.0.0.1:27017/?compressors=zlib&readPreference=primary&gssapiServiceName=mongodb&appname=MongoDB%20Compass&ssl=false')
"""
class ActionAutomation(Action):
    def name(self) -> Text:
        return "action_automate"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Welcome to first action program")
         return []
"""

class ActionknowledgeBase(Action):
    def name(self) -> Text:
        return "action_knowledge_base"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         text = tracker.latest_message['text']
         entities = tracker.latest_message['entities']
         print("My entities",entities)
         print("My text",text)

         for e in entities:
             if e['entity'] == 'knowledge':
                 name = e['value'].lower()

#                 print(name)
#             if name == "FTTP" or "fttp" :
#                 message = 'Fibre to the premises (FTTP) is a pure fibre connection from the exchange, into your business. It offers higher broadband speeds to specific premises in areas that have been enabled for FTTP (speeds up to 330/50MB/s)'
#             if name == "exchange":
#                 message = 'An exchange is a node in a telecommunications network that includes functions for access, control, switching, and charging of calls and other similar communication sessions.'
#             if name == "provide order":
#                 message = 'The provider order is a sales order with which you can sell products and services within the provider industry. For Ex: Broadband and NarrowBand Service Provisioning to the customers.'

         message =knowledge(name)
         dispatcher.utter_message(text=message)
         return []

class ActiongetQuery(Action):
    def name(self) -> Text:
        return "getQuery_automation"

#    @staticmethod
#    def required_slots(tracker : Tracker) -> List[Text]:
#        return ["Environment","ID","Journey_Name"]


    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict) -> List[Dict]:

             required_slots["Environment","Journey_Name"]
             print(required_slots)
             for slot_name in required_slots:
                 if tracker.slots.get(slot_name) is None:
                     return [SlotSet("Required slot",slot_name)]

             return [SlotSet("Required slot", None)]

class ActionSubmit(Action):
     def name(self) -> Text:
         return "action_submit"

     def run(self, dispatcher,
             tracker: Tracker,
             domain: "DomainDict",) -> List[Dict[Text, Any]]:

#             response = requests.get("http://127.0.0.1:5000/rpa",json={"Environment": tracker.get_slot('Environment'), "Journey Name": tracker.get_slot('Journey_Name')})
             dispatcher.utter_message(template="utter_details_thanks",Environment = tracker.get_slot('Environment'), Journey_Name = tracker.get_slot('Journey_Name') )
             return []

class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        temp=int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",
            tracker,temp=temp)

        return []

class ActiongetQuery(Action):
    def name(self) -> Text:
        return "getQuery_order"

    @staticmethod
    def required_slots_order(tracker : Tracker) -> List[Text]:
        return ["component"]

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict) -> List[Dict]:

             required_slots_order["component"]
             for slot_name in required_slots_order:
                 if tracker.slots.get(slot_name) is None:
                     return [SlotSet("Required slot",slot_name)]

             return [SlotSet("Required slot",None)]

class ActionSubmit2(Action):
     def name(self) -> Text:
         return "action_submit2"

     def run(self, dispatcher,
             tracker: Tracker,
             domain: "DomainDict",) -> List[Dict[Text, Any]]:

#             response = requests.get("http://127.0.0.1:5000/rpa",json={"Environment": tracker.get_slot('Environment'), "Journey Name": tracker.get_slot('Journey_Name')})
             dispatcher.utter_message(template="utter_details_thanks2",Component = tracker.get_slot('component'))
             return []


class ActionBrain(Action):
    def name(self) -> Text:
        return "action_brain_api"

    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        temp=response_processor_brain(text)
        dispatcher.utter_template("utter_brain_response",
            tracker,temp=temp)

        return []
