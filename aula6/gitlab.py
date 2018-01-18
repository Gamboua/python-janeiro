import requests, json


class Gitlab:
    token = 'y5BAhu9Tdmi84XjSY2yR'
    base_url = 'http://10.100.0.176'

    def get_projects(self):
        return json.loads(requests.get(
            "%s/api/v3/projects?private_token=%s" % 
            (self.base_url, self.token)
        ).text)

    def get_users(self):
        return json.loads(requests.get(
            "%s/api/v3/users?private_token=%s" % 
            (self.base_url, self.token)
        ).text)

    def new_user(self, data):
        return json.loads(requests.post(
            "%s/api/v3/users?private_token=%s" % 
            (self.base_url, self.token)
        , data=data).text)

    def new_project(self, data):
        return json.loads(requests.post(
            "%s/api/v3/projects?private_token=%s" % 
            (self.base_url, self.token)
        , data=data).text)


if __name__ == '__main__':
    obj = Gitlab()

    obj.new_project(
        {
            "name": "Projeto Beta"
        }
    )

    for i in obj.get_projects():
        print(i['name'])
    
    obj.new_user(
        {
            "name": "Gabriel",
            "email": "gabriel@gabriel.com",
            "username": "gabriel",
            "password": "4linux123"
        }
    )

    for i in obj.get_users():
        print(i['name'], i['username'])