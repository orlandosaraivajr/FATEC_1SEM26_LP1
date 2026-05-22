import pickle
import requests

url = "https://rickandmortyapi.com/api/character"
dados = requests.get(url).json()

with open("rick_morty.bin", "wb") as arquivo:
    pickle.dump(dados, arquivo)