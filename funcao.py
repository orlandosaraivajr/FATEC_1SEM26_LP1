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