# Receber os valores de num1 e num2
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

# Converter os valores num1 e num2 de texto (string) para número (inteiro)
num1 = int(num1)
num2 = int(num2)

# Somar os dois números e armazenar na variável soma
soma = num1 + num2

print('A soma de ' + str(num1) + ' e ' + str(num2) + ' é: ' + str(soma))