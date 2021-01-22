import requests

#sender = input("hi\n")
#
bot_message = ""
while bot_message != "Bye":
    message =input("User :")
    r = requests.post("http://localhost:5002/webhooks/rest/webhook", json ={"message": message})

    print("Bot :", end= '')
#    print(r.text)
    for i in r.json():
#        print(i)
        bot_message = i['text']
        print(f"{bot_message}")
