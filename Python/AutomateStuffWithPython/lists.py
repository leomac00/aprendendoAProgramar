# #Macete para adicionar valores contidas em listas a variaveis
# gato = ['gordo','cinza','velha']
# # inves de fazer isso:
# tamanho = gato[0]
# cor = gato[1]
# idade = gato[2]
# #Faça isso:
# tamanho, cor, idade = gato
#
# print(tamanho)
# print(cor)
# print(idade)
####################################
# #Testando In e Not:
# lista = ['cao','gato','periquito']
# spam = 'cao' in lista
# print(spam)
# spam = 'baleia' not in lista
# print(spam)
# spam = 'macaco' in lista
# print(spam)
####################################
# #Listagem de nomes de gatos
# catList = []
# while True:
#     print('Digite o nome do gato no. {} ou aperte enter para encerrar o processo.'.format(len(catList)+1))
#     name = input()
#     if name == '':
#         break
#     catList = catList + [name]
# print('Os nomes dos gatos sao:')
# for i in  range (0, len(catList)): #Aqui criei a variavel 'i' pois quis mostrar o numero do gato dentro da lista no print a seguir.
#     print('O gato no. {} se chama: {}'.format(i+1, catList[i]))
# # caso nao quisesse mostrar poderia ter feito apenas o seguinte:
# for name in catList:
#     print('Um dos gatos se chama: {}'.format(name))
####################################
# # slices em listas
# lista = ['oculos','celular','computador','garrafa','sanduiche','cerveja','café']
# print('lista original: {}'.format(lista))
# print('mostrando o slice do 0 ao 3 (lista[:3]): {}'.format(lista[:3]))
# print('mostrnado o slice do 3 ao 6 (lista[3:]): {}'.format(lista[3:]))
# print('mostrando o slice do 2 ao 5 (lista[2:5]): {}'.format(lista[2:5]))
####################################
#exemplo de listas
# lista2 = ['baiacu','baleia']
# lista1 = ['cachorro','gato','rato',lista2]
# print(lista2[0])
# print(lista1[3])
# print(lista1[3][0])
# print(lista1[-2])
####################################
#testando erros em listas...
# import random
# spam = 5
# lista = ["gato","rato"]
# try:
#     print(lista[spam])
# except TypeError:
#     print("erro no tipo do valor do argumento da lista, convertendo para int")
#     spam = int(round(spam))
# except IndexError:
#     spam = random.randint(0,len(lista)-1)
#     print("erro no indice da lista, acessando o indice aleatorio no. {} da lista".format(spam))
# finally:
#     print(lista[spam])
