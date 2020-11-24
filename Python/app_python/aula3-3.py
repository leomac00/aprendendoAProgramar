a=float(input('Digite a nota do primeiro bimestre: '))
b=float(input('Digite a nota do segundo bimestre: '))
c=float(input('Digite a nota do terceiro bimestre: '))
d=float(input('Digite a nota do quarto bimestre: '))
media=(a+b+c+d)/4
if 0<=a<=10 and 0<=b<=10 and 0<=c<=10 and 0<=d<=10:
    print('sua média é: {}'.format(media))
else:
    print('digite notas validas!')