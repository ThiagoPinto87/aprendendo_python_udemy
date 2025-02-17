# requests para requisições HTTP

# rodando servidor em python (No terminal digite o abaixo.)
# python -m http.server -d .\aula190\ 3333
# python -m http.server -d pasta ou arquivo\ porta

# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3001/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)  # conteúdo em byte.
# print(response.json())
print(response.text)
