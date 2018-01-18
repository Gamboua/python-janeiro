import requests
import json

#url = 'http://localhost:5000/usuarios/'
url = 'http://localhost:5000/usuarios/7/'
response = requests.get(url)

var = json.loads(response.text)

# for v in var['usuarios']:
#     print(v['nome'])

for key, value in var.items():
    print(key, value)

########## POST
url = 'http://localhost:5000/usuarios/'
data = json.dumps({"nome": "Joao", "email": "joao@joao.com"})
headers = {
    "Content-Type": "application/json"
}

# response = requests.post(url, data=data, headers=headers)

print(response)

########## PUT
url = 'http://localhost:5000/usuarios/7/'
data = json.dumps({"nome": "Joao", "email": "maria@joao.com"})
headers = {
    "Content-Type": "application/json"
}

response = requests.put(url, data=data, headers=headers)

print (response.text)

########## DELETE
url = 'http://localhost:5000/usuarios/7/'

response = requests.delete(url)

print (response.text)