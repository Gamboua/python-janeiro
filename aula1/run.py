from flask import Flask, jsonify
from Blueprints.UsuariosBlueprint import usuarios

app = Flask(__name__)
app.register_blueprint(usuarios)

@app.route("/")
def index():
    return "<table border='1'><tr><td>GABRIEL</td></tr></table>"


if __name__ == '__main__':
    app.run(debug=True)