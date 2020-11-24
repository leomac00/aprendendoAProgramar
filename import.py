import sys
while True:
    sair = str(input('digite "sair" para sair: '))
    if sair == 'sair':
        sys.exit()
#########################################
# from random import randint
# vezes = int(input('Quantas vezes deseja rolar o d20? : '))
# for i in range(vezes):
#     d20 = randint(1, 21)
#     if d20 == 20:
#         print('Acerto crítico! Você rolou: {}  =D'.format(d20))
#     elif d20 == 1:
#         print(print('Erro crítico! Você rolou: {}  =['.format(d20)))
#     else:
#         print('Você rolou: {} '.format(d20))
########################################
# import random
# vezes = int(input('Quantas vezes deseja rolar o d20? : '))
# for i in range(vezes):
#     d20 = random.randint(1, 21)
#     if d20 == 20:
#         print('Acerto crítico! Você rolou: {}  =D'.format(d20))
#     elif d20 == 1:
#         print(print('Erro crítico! Você rolou: {}  =['.format(d20)))
#     else:
#         print('Você rolou: {} '.format(d20))