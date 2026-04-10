'''
Faça um programa que percorra duas listas e gere uma
terceira lista sem elementos repetidos.
Exemplo:

lista1 = [1,2,3,4,2,3]
lista2 = [4,5,6,7]

Resultado:
lista3 = [1,2,3,4,5,6,7]
'''
lista1 = [1,2,3,4,2,3]
lista2 = [4,5,6,7]
lista3 = []

# Primeiro passo: percorro a lista1 e se o elemento
#  não estiver na lista3, adicionar.

for elemento in lista1:
    if not elemento in lista3:
        lista3.append(elemento)

# Segundo passo: Percorrer a lista2, e se o elemento
# não estiver na lista3, adicionar.

for elemento in lista2:
    if not elemento in lista3:
        lista3.append(elemento)

print(lista3)

# Segundo método: 
lista4 = []
lista4 = list(set(lista1 + lista2))
print(lista4)