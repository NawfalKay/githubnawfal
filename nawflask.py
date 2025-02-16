from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods =['POST','GET'])
def entry_point():
    return jsonify(message="halo reja")


@app.route('/dimana',methods =['POST','GET'])
def dimana():
    return jsonify(message="dirumah lah kocak")


@app.route('/tanya',methods =['POST','GET'])
def tanya():
    if request.method == 'POST':
        body = request.get_json()
        print(body['lu suka game apa'])
        return jsonify(message="dirumah lah kocak",data=body['lu suka game apa'])
    elif request.method == 'GET':
        return jsonify(message="dirumah lah kocak")
    



if __name__ == '__main__':
    app.run(debug=True)