from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS 
from pymongo import MongoClient

# .\venv\Scripts\activate.bat
# python src/app.py




app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://federico:federico@sportclub.elkxw.mongodb.net/sportclub?retryWrites=true&w=majority'
mongo = PyMongo(app)
CORS(app)

#  atlasdb
client = MongoClient("mongodb+srv://federico:federico@sportclub.elkxw.mongodb.net/sportclub?retryWrites=true&w=majority")
db = client.sportclub


dbusers = mongo.db.users
dbplanes = mongo.db.planes
dbclientes = mongo.db.clientes



#######  USERS  ########


@app.route('/users', methods=['POST'])
def createUsers():
    id = dbusers.insert({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password'],
    })
    return jsonify(str(ObjectId(id)))

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in dbusers.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'password': doc['password'],
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = dbusers.find_one({'_id': ObjectId(id)})
    print(user)
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password'],
    })

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    dbusers.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg':'user deleted'})
    
@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    dbusers.update_one({'_id': ObjectId(id)}, {'$set':{
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password'],
    }})
    return jsonify({'msg':'user updated'})


#######  PLANES  ########    

@app.route('/planes', methods=['POST'])
def createPlanes():
    id = dbplanes.insert({
        'name': request.json['name'],
        'precio': request.json['precio'],
    })
    return jsonify(str(ObjectId(id)))

@app.route('/planes', methods=['GET'])
def getPlanes():
    planes = []
    for doc in dbplanes.find():
        planes.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'precio': doc['precio']
        })
    return jsonify(planes)


@app.route('/planes/<id>', methods=['GET'])
def getPlan(id):
    plan = dbplanes.find_one({'_id':ObjectId(id)})
    print(plan)
    return jsonify({
        '_id': str(ObjectId(plan['_id'])),
        'name': plan['name'],
        'precio': plan['precio'],
    })

@app.route('/planes/<id>', methods=['DELETE'])
def deletePlan(id):
    dbplanes.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'plan deleted'})

@app.route('/planes/<id>', methods=['PUT'])
def updatePlan(id):
    dbplanes.update_one({'_id': ObjectId(id)}, {'$set':{
        'name': request.json['name'],
        'precio': request.json['precio'],
    }})
    return jsonify({'msg':'plan updated'})


#######  CLIENTES  ########

@app.route('/clientes', methods=['POST'])
def createClientes():
    id = dbclientes.insert({
        'plan_asociado': request.json['plan_asociado'],
        'status': request.json['status'],
        'fecha_suscripcion': request.json['fecha_suscripcion'],
        'fecha_vigencia': request.json['fecha_vigencia']
    })
    return jsonify(str(ObjectId(id)))

@app.route('/clientes', methods=['GET'])
def getClientes():
    clientes = []
    for doc in dbclientes.find():
        clientes.append({
            '_id': str(ObjectId(doc['_id'])),
            'plan_asociado': doc['plan_asociado'],
            'status': doc['status'],
            'fecha_suscripcion': doc['fecha_suscripcion'],
            'fecha_vigencia': doc['fecha_vigencia']
        })
    return jsonify(clientes)

@app.route('/clientes/<id>', methods=['GET'])
def getCliente(id):
    cliente = dbclientes.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(cliente['_id'])),
        'plan_asociado': cliente['plan_asociado'],
        'status': cliente['status'],
        'fecha_suscripcion': cliente['fecha_suscripcion'],
        'fecha_vigencia': cliente['fecha_vigencia'],

    })

@app.route('/clientes/<id>', methods=['DELETE'])
def deleteCliente(id):
    dbclientes.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'cliente deleted'})

@app.route('/clientes/<id>', methods=['PUT'])
def updateCliente(id):
    dbclientes.update_one({'_id': ObjectId(id)}, {'$set':{
        'plan_asociado': request.json['plan_asociado'],
        'status': request.json['status'],
        'fecha_suscripcion': request.json['fecha_suscripcion'],
        'fecha_vigencia': request.json['fecha_vigencia'],
    }})
    return jsonify({'msg':'cliente updated'})


if __name__ == "__main__":
    app.run(debug=True)