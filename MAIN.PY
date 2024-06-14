'''Crie um programa que cadastre o nome de 30 alunos em uma lista, e receba de cada aluno 5 notas de 0 a 10. 
O programa deverá retornar a média do aluno e indicar se o aluno está aprovado ou reprovado (média para aprovação = 7). 
Ao final, o programa deverá mostrar uma lista com o nome dos aprovados. Crie um repositório, suba no GitHub e poste o link.'''

# lista de dicionários
nomes = []
notas = []
for i in range (30):
    nome = input(f' Informe seu nome {i+1}: ')
# novos dados são inseridos 
    nomes. append (nome)
    nota1 = float(input("Insira a nota 1: "))
    while nota1 < 0 or nota1 > 10:
        print ("Nota invalida, digite um numero entre 0 e 10")
        nota1 = float (input("Insira a nota 1: "))

    nota2 = float(input("Insira a nota 2: "))
    while nota2 < 0 or nota2 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota2 = float (input("Insira a nota 2: "))

    nota3 = float (input("Insira a nota 3: "))
    while nota3 < 0 or nota3 > 10:
        print ("Nota invalida, digite um numero entre 0 e 10")
        nota3 = float(input("Insira a nota 3: "))

    nota4 = float(input("Insira a nota 4: "))
    while nota4 < 0 or nota4 > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota4 = float (input ("Insira a nota 4: "))

    nota5 = float(input ("Insira a nota 5: "))
    while nota5 < 0 or notas > 10:
        print("Nota invalida, digite um numero entre 0 e 10")
        nota5 = float (input("Insira a nota 5: "))

    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    print ('A média final é:',media)
    if media >= 7:
        print ('Aprovado')
    else:
            print('Reprovado')

    notas.append([nome, [nota1, nota2, nota3, nota4, nota5], media,])

    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'Nn':
        break



#exibe a lista
for dado in nome:
    print(nome, notas)