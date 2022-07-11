import requests
import json

try:
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = json.loads(req.text)
    for user in data:
        f = open("data.txt", "a")
        f.write("User " + str(user['id']) + " is " + user['title'] + "\n")
        f.close()
        print("Arquivo criado!")
except :
    print("Erro na conexão")
    exit()

