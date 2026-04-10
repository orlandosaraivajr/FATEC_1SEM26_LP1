'''
Faça um programa que receba duas notas de seis alunos e calcule a média de cada aluno.
Para cada aluno, classifique-o conforme a tabela, mostrando a condição do aluno.
'''

lista_notas = []
TOTAL_ALUNOS = 6

x = 0
while x < TOTAL_ALUNOS:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    lista_notas.append([nota1, nota2])
    x = x + 1
    
print(lista_notas)

x = 0
while x < len(lista_notas):
    media = (lista_notas[x][0] + lista_notas[x][1]) / 2
    if media < 3:
        print('Reprovado')
    if media >= 3 and media < 7:
        print('Exame')
    if media >= 7:
        print('Aprovado')
    x = x + 1