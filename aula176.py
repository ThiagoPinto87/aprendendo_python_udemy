# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# Aqui foi usado o typing para poder facilitar a leitura do arquivo json que foi importado usando o loads do "import json"

filme: Movie = json.loads(string_json)
# pprint(filme, width=40)
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year'] + 10)


# Aqui está sendo exportado o arquivo python para json usando a função dumps e os metodos ensure_ascii para poder permitir acentuações e usando também a identação e selecionado com 2 espaços.
json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)
