print('digite seu nome e entao pressione ENTER')
nome=input()
if nome=='leo':
    print('qual a senha?')
    senha=input()
    if senha=='admin':
        print('certa resposta!')
    else:
        print('senha invalida')
else:
    print('bom dia, '+nome+' !')
print(' qual a sua idade?')
idade=int(input())
if idade<18:
    print('voce é só um menino! fui eu que te criei!')
elif idade>=18:
    print('voce eh de maior, já pode ir preso hahahaha')
