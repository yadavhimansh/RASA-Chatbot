import requests
from pymongo import MongoClient
from Text_cleaning import text_cleaning

def knowledge(text):
    client = MongoClient('mongodb://127.0.0.1:27017/?compressors=zlib&readPreference=primary&gssapiServiceName=mongodb&appname=MongoDB%20Compass&ssl=false')
    entities = text.lower()
    result = client['NLP_Engine']['FAQ'].find_one({'Intent': entities})
    message = []
    for key,value in result.items():
        if(key == 'Answer'):
            message= value

    return message
