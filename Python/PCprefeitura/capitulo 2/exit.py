import sys
import random
while True:
    print('seu numero da loteria é: ' + str(random.randint(0,99999999)))
    print('deseja sair? digite "sair" se sim')
    resposta=input()
    if resposta=='sair':
        sys.exit()
    print('voce decidiu ficar')
