from flask import Blueprint, jsonify

usuarios = Blueprint('usuarios', __name__)

@usuarios.route("/usuarios/")
def index():
    return jsonify({
        "mensagem": "Listando todos os usuarios"
    })

@usuarios.route("/usuarios/<id>/")
def usuario_get(id):
    return "Listando aluno %s" % id

@usuarios.route("/usuarios/", methods=["POST"])
def usuarios_post():
    return "Adicionando novo usuario"