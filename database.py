from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://delgadocristhiandd:0GD8VQN9jGhyphEl@examen.8vej6od.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_proyecto_final"]
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db