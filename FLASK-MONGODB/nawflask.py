from flask import Flask,jsonify,request

app = Flask(__name__)

################################## PYMONGO SECTION ##############################################################################
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nawfalkasyanre:vZBuRQ6g4MZBJdNq@cluster0.3tnvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))


db = client['DatabasePhaethon']
my_collections = db['sensordata'] # ganti sesuai dengan nama

def store_data(data): 
    results = my_collections.insert_one(data) 
    return results.inserted_id

def get_data(): 
    get_result = my_collections.find() 
    return get_result 


################################################################################################################################

######################################## FLASK SECTION #########################################################################

@app.route('/',methods =['POST','GET'])
def entry_point():
    return jsonify(message="halo reja")

@app.route('/dimana',methods =['POST','GET'])
def dimana():
    return jsonify(message="dirumah lah kocak")





@app.route('/sensor1',methods =['POST','GET'])
def simpan_data_sensor():
    if request.method == 'POST':
        body = request.get_json()
        temperature = body['temperature']
        humidity = body['humidity']        
        timestamp = body['timestamp']
        data_final = {
            "temperature":temperature,
            "humidity" :humidity,
            "timestamp" :timestamp,
        }

        id = store_data(data_final)
        return{
            "message": f"Hai, saya akan memproses data anda {id}"
        }



    elif request.method == 'GET':
        return jsonify(message="dirumah lah kocak")
    



if __name__ == '__main__':
    app.run(debug=True)