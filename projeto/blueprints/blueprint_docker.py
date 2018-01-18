from flask import Blueprint, render_template, redirect
from models.docker_api import Docker

docker_blue = Blueprint('docker', __name__)

@docker_blue.route('/docker/')
def index():
    docker = Docker()
    containers = docker.get_containers()

    return render_template(
        'docker_containers.html',
        containers=containers
    )

@docker_blue.route('/docker/start/<name>/')
def docker_start(name):
    docker = Docker()
    docker.start_container(name)

    return redirect('/docker/')

@docker_blue.route('/docker/stop/<name>/')
def docker_stop(name):
    print(name)
    docker = Docker()
    docker.stop_container(name)

    return redirect('/docker/')