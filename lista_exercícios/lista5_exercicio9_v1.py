'''
Faça um programa que receba duas notas de seis alunos e calcule a média de cada aluno.
Para cada aluno, classifique-o conforme a tabela, mostrando a condição do aluno.
'''

nota1 = [0,0,0,0,0,0]
nota2 = [0,0,0,0,0,0]

x = 0
while x < 6:
    nota1[x] = float(input('Digite a primeira nota do aluno: '))
    nota2[x] = float(input('Digite a segunda nota do aluno: '))
    x = x + 1

print(nota1)
print(nota2)

x = 0
while x < 6:
    media = (nota1[x] + nota2[x]) / 2
    if media < 3:
        print('Reprovado')
    if media >= 3 and media < 7:
        print('Exame')
    if media >= 7:
        print('Aprovado')
    x = x + 1