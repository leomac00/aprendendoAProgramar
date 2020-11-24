continuar=True
while continuar==True:
    print('digite seu nome')
    nome=input()
    if nome=='seu nome':
        print('exatamente!')
        print('qual a senha?')
        senha=input()
        if senha=='senha':
            print('vc é o bichao mesmo!')
            break
        else:
            print('digitou errado, OTÁRIO!')
            print('deseja tentar novamente? s=sim;n=não')
            continuar=input()
            if continuar=='s':
                continuar=True
            elif continuar=='n':
                continuar==False
            else:
                print('digite um valor válido')
           
