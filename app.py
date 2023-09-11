from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from flask_pymongo import PyMongo
import database as dbase  
from persona import Persona
import requests

db = dbase.dbConnection()

app = Flask(__name__)

URL = "https://randomuser.me/api"
b= 1

@app.route('/',methods = ['GET','POST'])
def home():
        persons = db['persons']
        if request.method == 'GET':
               return render_template('index.html')
        if b==1:
                Data = requests.get(URL)
                DataPersona = Data.json()

                for e in DataPersona['results']:
                       genero=(e['gender'])
                       titulo=(e['name']['title'])
                       nombre=(e['name']['first'])
                       apellido=(e['name']['last'])
                person = Persona(genero,titulo,nombre,apellido)
                persons.insert_one(person.toDBCollection())
                return render_template('index.html',data = DataPersona['results'])
        else:
                return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True,port=8080)

   