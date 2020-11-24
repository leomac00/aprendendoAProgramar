numero=int(input('Digite um numero: '))
div = 0
for x in range (1,numero+1):
    resto = numero % x
    if resto == 0:
        div += 1
if div == 2:
    print('{} é um numero primo.'.format(numero))
else:
    print('{} nao é um numero primo.'.format(numero))
while True:
    escolha = input('deseja saber quais os numeros primos até {}? y=Sim / n=Não: '.format(numero))
    if escolha == 'n':
        print('Até mais!!!')
        break
    elif escolha == 'y':
        for num in range(numero+1):
            div=0
            for x in range(1,num+1):
                if num % 2 != 0:
                    resto = num % x
                    if resto == 0:
                        div+=1
                if div==2:
                        print(num)
        print('Até mais!!!')
        break