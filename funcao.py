# Função sem retorno

def soma(numero1, numero2):
    print('Somando')
    numero3 = numero1 + numero2
    print(numero3)

soma(10, 5)
soma(2, 5)

# Função COM retorno
# Usando a palavra return

def soma2(numero1, numero2):
    print('Somando')
    numero3 = numero1 + numero2
    return numero3

c = soma2(10, 5)
print(c)
c = soma2(2, 5)
print(c)

'''
Atividade 1:
Criar uma função chamada "maior" que recebe 
dois números e mostra qual o maior
'''
def maior(numero1, numero2):
    if numero1 > numero2:
        print(numero1)
    elif numero2 > numero1:
        print(numero2)
    else:
        print("Números iguais")

maior(10, 4)
maior(3, 6)
maior(4, 4)

'''
Atividade 2:
Criar uma função chamada "maior2" que recebe 
dois números e retorna qual o maior
'''
