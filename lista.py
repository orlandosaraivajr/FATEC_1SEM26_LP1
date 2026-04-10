'''
Problema 1 que fizemos juntos
'''
notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input("Digite uma nota: "))
    soma = soma + notas[x]
    x = x + 1
# media = round(soma/x, 2)
print(f'Média: {soma/x: 5.2f}')
print(f'Média: {soma/x}')