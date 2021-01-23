from pymongo import MongoClient
#from werkzeug.security import generate_password_hash

client = MongoClient("write the path where you can get the data in mongodb")

# =============================================================================
chat_db = client.get_database("Chatbot")
users_collection = chat_db.get_collection("User_history")
#
print(users_collection)
#
def save_user(username, email):
    users_collection.insert_one({'_id': username, 'email': email})

save_user('Himanshu','abc@com')  
