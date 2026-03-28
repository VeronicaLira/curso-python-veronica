#Aula 05 - Revisão de listas

# listaNome=['Maria', 'Pedro', 'João']
# listaNome[0] = 'Juliana'

# print(listaNome)

# for nome in listaNome:
#     print(nome)


#Crie uma lista com 10 números e use o for para printar na tela cada um dos 10 números
# print('Questão 1')

# listaNumeros=[1,2,3,4,5,6,7,8,9,10]

# for numero in listaNumeros:
#     print(numero)

#A partir da primeira lista, use um for para percorrer a lista e printar os números maiores que 5

# print('Questão 2')

# for numero in listaNumeros:
#     if numero > 5:
#             print(numero)


#Funções internas de listas

#append()--> Acrescentar no final de uma lista
#insert (0,item) --> Acrescenta em uma posição
#pop() --> Deleta o ultimo item da lista
#pop(0) --> Deleta de uma posição
#del(lista[x:y]) --> Deleta um intervalo de uma lista

#1. Crie uma lista vazia chamada aprovados. Peça para o usuário digitar 5 notas, e para cada nota: se a nota for maior ou igual a 7, adicione na lista aprovados caso contrário, ignore.

# aprovados = []
# for i in range (5):
#     nota = float(input('Digite a nota:'))
#     if nota >= 7:
#         aprovados.append(nota)
# print(aprovados)

#2. Dada a lista: valores = [5, 12, 7, 20, 3, 15]. Percorra a lista e remova todos os números menores que 10. Mostre a lista com o resultado final.

# valores = [5, 12, 7, 20, 3, 15]
# valorMaior = []

# for valor in valores:
#      if valor >= 10:
#           valorMaior.append(valor)
# valores = valorMaior

# print(valores)

#Dicionários

# pessoa = {
#     "nome":"Maria",
#     "idade":20,
#     "cidade":"Fortaleza"
# }

# print(pessoa)
# print(pessoa["idade"])


#Crie um dicionário chamado aluno e salve o nome, o curso e a média desse aluno recebendo esses dados do teclado (usando o input)
nome = input('Nome:')
curso = input('Curso:')
media = float(input('Média:'))

aluno = {
    "Nome":nome,
    "Curso":curso,
    "Média":media
}

print(aluno)

print(f'Olá {aluno["Nome"]} seja bem-vindo ao curso de {aluno["Curso"]} sua média é : {aluno["Média"]}')

