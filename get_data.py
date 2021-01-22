from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://127.0.0.1:27017/?compressors=zlib&readPreference=primary&gssapiServiceName=mongodb&appname=MongoDB%20Compass&ssl=false')
filter={}

result = client['NLP_Engine']['FAQ'].find(
  filter=filter
)

for i in result:
    print(i)
