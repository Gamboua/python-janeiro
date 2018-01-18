from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db": "dexter-api"}
db = MongoEngine(app)


class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(default=datetime.now())