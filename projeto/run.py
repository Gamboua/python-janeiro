from flask import Flask, render_template
from blueprints.blueprint_docker import docker_blue

app = Flask(__name__)
app.register_blueprint(docker_blue)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)