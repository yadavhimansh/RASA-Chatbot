from pymongo import MongoClient
#from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://test:test@chatapp.4bdmu.mongodb.net/test?retryWrites=true&w=majority")

# =============================================================================
chat_db = client.get_database("Chatbot")
users_collection = chat_db.get_collection("User_history")
#
print(users_collection)
#
def save_user(username, email):
    users_collection.insert_one({'_id': username, 'email': email})

save_user('Himanshu','abc@com')  
