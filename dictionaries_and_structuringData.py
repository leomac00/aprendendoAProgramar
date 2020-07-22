# #Jogo da velha / tic-tac-toe
# theBoard = {
#     'top-L':' ','top-M':' ','top-R':' ',
#     'mid-L':' ','mid-M':' ','mid-R':' ',
#     'low-L':' ','low-M':' ','low-R':' '
# }
# def printBoard(board):
#     print('{}|{}|{}'.format(board['top-L'],board['top-M'],board['top-R']))
#     print('-+-+-')
#     print('{}|{}|{}'.format(board['mid-L'],board['mid-M'],board['mid-R']))
#     print('-+-+-')
#     print('{}|{}|{}'.format(board['low-L'],board['low-M'],board['low-R']))
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Vez de: ' + turn + '. Qual espaço deseja colocar sua peça? ')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

######################################################

# #Esse programa mostra a quantidade de cada letra em uma dada frase e usa o modulo pprint
# import pprint
# text = 'Eu gosto de sorvete de banana'
# count = {}
# for character in text:
#     count.setdefault(character,0)
#     count[character] += 1
# pprint.pprint(count)

######################################################

# #Esse programa mostra a quantidade de cada letra em uma dada frase
# text = 'Eu gosto de sorvete de banana'
# count = {}
# for character in text:
#     count.setdefault(character,0)
#     count[character] += 1
# print(count)

######################################################

# mochila = {'caderno':2,'caneta':2,'celular':1} #exemplo de dicionario
# print('Estou levando {caneta} canetas e {maca} maçãs na minha mochila.'.format(caneta =  mochila.get('caneta', 0),maca = mochila.get('macas', 0)))

######################################################
#
# animais = {'felino': 'gato', 'canino':'cachorro'} #exemplo de dicionario
#
# for i in animais.values(): #'.value()' retorna os valores dentro de cada key
#     print(i)
#
# for j in animais.keys(): #'.keys()' retorna os valores das keys dentro do dicionario
#     print(j)
#
# for k in animais.items(): #'.items()' retorna cada item (keys e respectivos valores) do dict
#     print(k)