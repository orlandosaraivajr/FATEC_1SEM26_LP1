'''
Faça um programa que leia duas listas e que gere uma
terceira lista com os elementos das duas primeiras listas.
'''

lista1 = []
lista2 = []

for x in range(5):
    print("Digitando um elemento ...")
    elemento = input('Digite um elemento: ')
    lista1.append(elemento)


for x in range(6):
    print("Digitando um elemento para a segunda lista ...")
    elemento = input('Digite um elemento: ')
    lista2.append(elemento)

print(lista1)
print(lista2)

lista3 = []

# Percorrer as duas listas e append na lista3
for x in lista1:
    lista3.append(x)

for x in lista2:
    lista3.append(x)
    
print(lista3)

# Adicionando a lista 4
lista4 = []
lista4 = lista1 + lista2
print(lista4)