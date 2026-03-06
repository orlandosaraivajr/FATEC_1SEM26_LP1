idade = input("Digite sua idade: ")
idade = int(idade)

if idade >= 18:
    print('Maior de idade ')
else:
    print('Menor de idade')

'''
Se a idade for menor de 14 anos, não pode entrar
Se a idade for entre 14 e 18, pode entrar com os pais
Se for maior que 18, pode entrar
'''
if idade >= 18:
    print('Pode entrar na festa')
elif idade >= 14 and idade < 18:
    print('Pode entrar com os pais')
else:
    print('Não pode entrar')

print('Versão 2')

if idade >= 18:
    print('Pode entrar na festa')
elif idade >= 14:
    print('Pode entrar com os pais')
else:
    print('Não pode entrar')


print('Versão 3')

if idade >= 18:
    print('Pode entrar na festa')
else:
    if idade >= 14:
        print('Pode entrar com os pais')
    else:
        print('Não pode entrar')