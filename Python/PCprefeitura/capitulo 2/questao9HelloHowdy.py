resposta='sim'
while resposta=='sim':
    print('digite "1" ou "2"')
    texto=input()
    if texto=='1':
        print('Hello')
        print('deseja continuar aqui? se sim, digite "sim"')
        resposta=input()
    elif texto=='2':
        print('Howdy!')
        print('deseja continuar aqui? se sim, digite "sim"')
        resposta=input()
    else:
        print('voce digitou tudo errado, OTÁRIO!')
        print('deseja continuar aqui? se sim, digite "sim"')
        resposta=input()
        
