from flask import Flask, render_template, request, redirect
from models.models import Usuario
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usuarios/")
def usuarios():
    usuarios = json.loads(Usuario.objects().to_json())

    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/<email>/", methods=['POST', 'GET'])
def usuarios_busca(email):
    usuario = Usuario.objects(email=email).first()

    if request.method == 'POST':
        usuario.email = request.form['email']
        usuario.nome = request.form['nome']

        usuario.save()

    usuario = json.loads(usuario.to_json())

    return render_template("usuarios_busca.html", usuario=usuario)

@app.route("/usuarios/deletar/<email>/")
def usuario_delete(email):
    usuario = Usuario.objects(email=email).first()

    usuario.delete()

    return redirect('/usuarios/')

@app.route("/usuarios/inserir/", methods=["GET", "POST"])
def usuario_inserir():
    if request.method == 'POST':
        user = Usuario()
        user.email = request.form['email']
        user.nome = request.form['nome']

        user.save()

        return redirect('/usuarios/')

    return render_template('usuario_inserir.html')


if __name__ == '__main__':
    app.run(debug=True)