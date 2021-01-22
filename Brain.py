import requests

def response_processor_brain(text):
#    return "Thanks! we are processing the request"
    response = requests.get("http://127.0.0.1:5000/brain",data=text)
    return response.text
