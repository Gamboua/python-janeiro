from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db": "dexter-api"}

db = MongoEngine(app)

class Usuario(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(default=datetime.now())


if __name__ == '__main__':
    usuario = Usuario()
    usuario.nome = "Gabriel"
    usuario.email = "gabriel@gabriel.com.br"

    usuario.save()