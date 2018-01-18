from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usuarios/")
def usuarios():

    usuarios = [
        {
            "id": 1,
            "nome": "Gabriel da Silva",
            "email": "gabriel@4linux.com.br"
        },
        {
            "id": 2,
            "nome": "Joao da Silva",
            "email": "joao@4linux.com.br"
        }
    ]

    print(usuarios)

    return render_template("usuarios.html", usuarios=usuarios)


if __name__ == '__main__':
    app.run(debug=True)