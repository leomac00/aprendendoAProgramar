grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for a in range (0, len(grid)):
    for b in range (0, len(grid)):
        print(grid[b][a])

##########################################
# #Projeto do capitulo 4
# lista = ['bacon','ovos','salada','feijao']
# print(' e '.join(lista))
##########################################
# #Bola 8 usando listas
# import random
# i = random.randint(0,7)
# bola8 = ["Com certeza sim","Sim","Talvez","Nem pense nisso","Volte mais tarde","Se concentre mais e pergunte novamente","Impossível","Nao"]
# # print(i)
# print(bola8[i])
##########################################
# # exemplo de append(), insert() e remove()
# lista = ['baleia','cachorro','gato']
# lista.append('macaco')
# print(lista)
# lista.insert(0,'periquito')
# lista.append('gato')
# print(lista)
# lista.remove('gato')
# print(lista)
##########################################
# # Esse programa demonstra um método (index()) aplicado a listas.
# lista = ['baleia','cachorro','gato']
# spam = lista.index('cachorro')
# print(spam)