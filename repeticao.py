print(1)
print(2)
print(3)

# While
print('Usando while')
x = 1
while x <= 3:
    print(x)
    x = x + 1

# Lançamento do foguete
N = input("Digite um número")
N = int(N)

while N > 0:
    print(N)
    N = N - 1
print("Liberar o Vôo")

n = 1 # n está atuando como um contador
soma = 0 # variável soma está atuando como um acumulador
while n <= 10:
    x = int(input(f'Digite o {n} número: '))
    soma = soma + x
    n = n + 1

print(soma)

n = 1 # n está atuando como um contador
soma = 0 # variável soma está atuando como um acumulador
'''
while n <= 10:
    x = int(input(f'Digite o {n} número: '))
    soma += x # Mesma coisa que soma = soma + x
    n += 1 # Mesma coisa que  n = n + 1

print(soma)
'''

# Condição de parada
s = 0
while True:
    v = int(input('Digite um valor: '))
    if v == 0:
        break
    s = s + v
print(s)

for x in range(5):
    print(x + 1)