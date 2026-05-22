"""
Avaliação — 1º Semestre
Manipulação de Dados com Python
Tema: API Rick and Morty
Objetos utilizados: list, tuple, dict, set, string, numbers
"""


# =============================================================================
# EXERCÍCIO 1 — Contar espécies únicas
# =============================================================================
# Implemente uma função chamada contar_especies que recebe um dicionário no
# formato da API Rick and Morty (com a chave "results") e retorna um dicionário
# onde as chaves são as espécies encontradas e os valores são a quantidade de
# personagens de cada espécie.
#
# Exemplo 1:
#   Entrada: {"results": [{"name": "Rick", "species": "Human"},
#                         {"name": "Morty", "species": "Human"},
#                         {"name": "Birdperson", "species": "Bird-Person"}]}
#   Saída:   {"Human": 2, "Bird-Person": 1}
#
# Exemplo 2:
#   Entrada: {"results": [{"name": "Mr. Meeseeks", "species": "Alien"},
#                         {"name": "Squanchy", "species": "Cat-Person"},
#                         {"name": "Alien", "species": "Alien"}]}
#   Saída:   {"Alien": 2, "Cat-Person": 1}
# =============================================================================

def contar_especies(dados):
    contagem = {}
    for p in dados["results"]:
        especie = p["species"]
        if especie in contagem:
            contagem[especie] += 1
        else:
            contagem[especie] = 1
    return contagem


# =============================================================================
# EXERCÍCIO 2 — Filtrar por status
# =============================================================================
# Implemente uma função chamada filtrar_por_status que recebe um dicionário no
# formato da API e uma string com o status desejado ("Alive", "Dead" ou
# "unknown"). A função deve retornar uma lista com os nomes dos personagens
# que possuem aquele status.
#
# Exemplo 1:
#   Entrada: dados = {"results": [{"name": "Rick", "status": "Alive"},
#                                 {"name": "Beth", "status": "Alive"},
#                                 {"name": "Birdperson", "status": "Dead"}]},
#            status = "Alive"
#   Saída:   ["Rick", "Beth"]
#
# Exemplo 2:
#   Entrada: dados = {"results": [{"name": "Rick", "status": "Alive"},
#                                 {"name": "Birdperson", "status": "Dead"},
#                                 {"name": "Noob Noob", "status": "unknown"}]},
#            status = "Dead"
#   Saída:   ["Birdperson"]
# =============================================================================

def filtrar_por_status(dados, status):
    pass


# =============================================================================
# EXERCÍCIO 3 — Extrair nomes em maiúsculo
# =============================================================================
# Implemente uma função chamada nomes_maiusculo que recebe um dicionário no
# formato da API e retorna uma lista com os nomes de todos os personagens
# convertidos para letras maiúsculas.
#
# Exemplo 1:
#   Entrada: {"results": [{"name": "Rick Sanchez"}, {"name": "Morty Smith"}]}
#   Saída:   ["RICK SANCHEZ", "MORTY SMITH"]
#
# Exemplo 2:
#   Entrada: {"results": [{"name": "Beth Smith"}, {"name": "Jerry Smith"},
#                         {"name": "Summer Smith"}]}
#   Saída:   ["BETH SMITH", "JERRY SMITH", "SUMMER SMITH"]
# =============================================================================

def nomes_maiusculo(dados):
    pass


# =============================================================================
# EXERCÍCIO 4 — Agrupar por gênero
# =============================================================================
# Implemente uma função chamada agrupar_por_genero que recebe um dicionário no
# formato da API e retorna um dicionário onde cada chave é um gênero ("Male",
# "Female", etc.) e o valor é uma lista com os nomes dos personagens daquele
# gênero.
#
# Exemplo 1:
#   Entrada: {"results": [{"name": "Rick", "gender": "Male"},
#                         {"name": "Summer", "gender": "Female"},
#                         {"name": "Morty", "gender": "Male"}]}
#   Saída:   {"Male": ["Rick", "Morty"], "Female": ["Summer"]}
#
# Exemplo 2:
#   Entrada: {"results": [{"name": "Beth", "gender": "Female"},
#                         {"name": "Alien X", "gender": "unknown"},
#                         {"name": "Jerry", "gender": "Male"}]}
#   Saída:   {"Female": ["Beth"], "unknown": ["Alien X"], "Male": ["Jerry"]}
# =============================================================================

def agrupar_por_genero(dados):
    pass


# =============================================================================
# EXERCÍCIO 5 — Calcular média de IDs
# =============================================================================
# Implemente uma função chamada media_ids que recebe um dicionário no formato
# da API e retorna a média aritmética dos IDs de todos os personagens da lista
# como um número de ponto flutuante.
#
# Exemplo 1:
#   Entrada: {"results": [{"id": 1, "name": "Rick"},
#                         {"id": 2, "name": "Morty"},
#                         {"id": 3, "name": "Summer"}]}
#   Saída:   2.0
#
# Exemplo 2:
#   Entrada: {"results": [{"id": 10, "name": "Beth"},
#                         {"id": 20, "name": "Jerry"}]}
#   Saída:   15.0
# =============================================================================

def media_ids(dados):
    pass


# =============================================================================
# EXERCÍCIO 6 — Remover duplicatas de espécies
# =============================================================================
# Implemente uma função chamada especies_unicas que recebe um dicionário no
# formato da API e retorna uma lista com as espécies presentes nos personagens,
# sem repetições e em ordem alfabética. Utilize um conjunto (set) durante o
# processamento.
#
# Exemplo 1:
#   Entrada: {"results": [{"species": "Human"}, {"species": "Alien"},
#                         {"species": "Human"}, {"species": "Robot"}]}
#   Saída:   ["Alien", "Human", "Robot"]
#
# Exemplo 2:
#   Entrada: {"results": [{"species": "Cronenberg"}, {"species": "Human"},
#                         {"species": "Cronenberg"}]}
#   Saída:   ["Cronenberg", "Human"]
# =============================================================================

def especies_unicas(dados):
    pass


# =============================================================================
# EXERCÍCIO 7 — Criar tuplas de identificação
# =============================================================================
# Implemente uma função chamada tuplas_personagens que recebe um dicionário no
# formato da API e retorna uma lista de tuplas. Cada tupla deve conter três
# elementos: (id, nome, status) de cada personagem, nessa ordem.
#
# Exemplo 1:
#   Entrada: {"results": [{"id": 1, "name": "Rick", "status": "Alive"},
#                         {"id": 2, "name": "Morty", "status": "Alive"}]}
#   Saída:   [(1, "Rick", "Alive"), (2, "Morty", "Alive")]
#
# Exemplo 2:
#   Entrada: {"results": [{"id": 5, "name": "Birdperson", "status": "Dead"}]}
#   Saída:   [(5, "Birdperson", "Dead")]
# =============================================================================

def tuplas_personagens(dados):
    pass


# =============================================================================
# EXERCÍCIO 8 — Verificar personagem existente
# =============================================================================
# Implemente uma função chamada personagem_existe que recebe um dicionário no
# formato da API e uma string com um nome de personagem. A função deve retornar
# True se o nome existir na lista (ignorando maiúsculas/minúsculas) ou False
# caso contrário.
#
# Exemplo 1:
#   Entrada: dados = {"results": [{"name": "Rick Sanchez"},
#                                 {"name": "Morty Smith"}]},
#            nome = "morty smith"
#   Saída:   True
#
# Exemplo 2:
#   Entrada: dados = {"results": [{"name": "Rick Sanchez"},
#                                 {"name": "Morty Smith"}]},
#            nome = "Jerry Smith"
#   Saída:   False
# =============================================================================

def personagem_existe(dados, nome):
    pass


# =============================================================================
# EXERCÍCIO 9 — Indexar por ID
# =============================================================================
# Implemente uma função chamada indexar_por_id que recebe um dicionário no
# formato da API e retorna um novo dicionário em que cada chave é o ID do
# personagem (número inteiro) e o valor é outro dicionário contendo apenas
# "nome" e "status" daquele personagem.
#
# Exemplo 1:
#   Entrada: {"results": [{"id": 1, "name": "Rick",
#                          "status": "Alive", "species": "Human"},
#                         {"id": 2, "name": "Morty",
#                          "status": "Alive", "species": "Human"}]}
#   Saída:   {1: {"nome": "Rick", "status": "Alive"},
#             2: {"nome": "Morty", "status": "Alive"}}
#
# Exemplo 2:
#   Entrada: {"results": [{"id": 5, "name": "Birdperson",
#                          "status": "Dead", "species": "Bird-Person"}]}
#   Saída:   {5: {"nome": "Birdperson", "status": "Dead"}}
# =============================================================================

def indexar_por_id(dados):
    pass


# =============================================================================
# EXERCÍCIO 10 — Resumo estatístico
# =============================================================================
# Implemente uma função chamada resumo_estatistico que recebe um dicionário no
# formato da API e retorna um dicionário com: total (número total de
# personagens), especies (quantidade de espécies únicas), vivos (personagens
# com status "Alive") e mortos (personagens com status "Dead").
#
# Exemplo 1:
#   Entrada: {"results": [{"status": "Alive", "species": "Human"},
#                         {"status": "Dead", "species": "Human"},
#                         {"status": "Alive", "species": "Alien"}]}
#   Saída:   {"total": 3, "especies": 2, "vivos": 2, "mortos": 1}
#
# Exemplo 2:
#   Entrada: {"results": [{"status": "Dead", "species": "Robot"},
#                         {"status": "Dead", "species": "Robot"},
#                         {"status": "unknown", "species": "Alien"}]}
#   Saída:   {"total": 3, "especies": 2, "vivos": 0, "mortos": 2}
# =============================================================================

def resumo_estatistico(dados):
    pass

import pickle

with open("rick_morty.bin", "rb") as arquivo:
    dados_rickandmortyapi = pickle.load(arquivo)

'''
print( 40 * '=')
print(contar_especies(dados_rickandmortyapi))
print( 40 * '=')
print(filtrar_por_status(dados_rickandmortyapi,'Alive'))
print(filtrar_por_status(dados_rickandmortyapi,'Dead'))
print(filtrar_por_status(dados_rickandmortyapi,'none'))
print( 40 * '=')
print(nomes_maiusculo(dados_rickandmortyapi))
print( 40 * '=')
print(agrupar_por_genero(dados_rickandmortyapi))
print( 40 * '=')
print(media_ids(dados_rickandmortyapi))
print( 40 * '=')
print(especies_unicas(dados_rickandmortyapi))
print( 40 * '=')
print(tuplas_personagens(dados_rickandmortyapi))
print( 40 * '=')
print(personagem_existe(dados_rickandmortyapi,'Rick'))
print(personagem_existe(dados_rickandmortyapi,'Rick Sanchez'))
print( 40 * '=')
print(indexar_por_id(dados_rickandmortyapi))
print( 40 * '=')
print(resumo_estatistico(dados_rickandmortyapi))
'''