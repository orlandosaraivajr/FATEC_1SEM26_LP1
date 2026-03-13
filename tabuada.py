numero = int(input("Digite um número: "))

for x in range(1,11):
    # print(str(numero) + ' x ' + str(x) + ' = ' + str(numero * x))
    # Usando f-strings
    print(f' {numero} x {x} = {numero * x}')