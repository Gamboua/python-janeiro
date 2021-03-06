from docker import Client


class Docker:
    def __init__(self):
        self.cli = Client(base_url="tcp://localhost:2376", version="auto")

    def get_containers(self, all=True):
        return [ c for c in self.cli.containers(all=all) ]

    def start_container(self, name):
        return self.cli.start(name)

    def stop_container(self, name):
        return self.cli.stop(name)

    def restart_container(self, name):
        return self.cli.restart(name)

    def create_container(self, name, command, image):
        return self.cli.create_container(
            name=name,
            command=command,
            image=image
        )

    def remove_container(self, name):
        return self.cli.remove_container(name)
        


if __name__ == '__main__':
    obj = Docker()
    
    # Mostrando todos os containers
    for i in obj.get_containers():
        print(i['Status'])

