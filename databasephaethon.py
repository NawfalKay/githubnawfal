
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nawfalkasyanre:vZBuRQ6g4MZBJdNq@cluster0.3tnvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))




db = client['DatabasePhaethon']
my_collections = db['sensordata'] # ganti sesuai dengan nama

# Data yang ingin dimasukkan
murid_1 = {'nama':'John Doe','Jurusan':'IPS','Nilai':90}
murid_2 = {'nama':'Jane Doe', 'Jurusan':'IPA','Nilai':85}

results = my_collections.insert_many([murid_2])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan



hasil =my_collections.find()
for x in hasil :
    print(x)







try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)