#este programa demonstra os algoritmos de decisao if/else/elif...
a=int(input('Digite o primeiro valor desejado: '))
b=int(input('Digite o segundo valor desejado: '))
c=int(input('Digite o terceiro valor desejado: '))
#aqui está como deve ser a sintaxe para os operadores logicos, atentar ao ':' que devem ser usados depois de qualquer if/else/elif
if a > b and a > c:
    print('O maior valor é {}'.format(a))
elif b > a and b > c:
    print('O maior valor é {}'.format(b))
else:
    print('O maior valor é {}'.format(c))