# Heart with grid project
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

spam = 0
eggs = 0
bacon = ''

for eggs in range (0,6): #as the book hints we should go row by row so that's why this first 'for'
    for spam in range (0,9):
        bacon += '{}  '.format(grid[spam][eggs]) # Here we swap rows with columns because we want to transpose it; we start by increasing the first value,that's why we use 'spam' first and 'eggs' on the second '[]' and then we proced to the next line.
    print('{}'.format(bacon)) # Here we print the line created for 'bacon'
    bacon = '' #then we need to reset this because otherwise it will stack multiple 'bacons' together
print('There`s our pretty heart!')
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