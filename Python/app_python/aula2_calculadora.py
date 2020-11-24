#este programa realiza alguns calculos de acordo com valores inseridos pelo usuario e os mostra para ele
#perceba a maneira como as duas proximas linhas fazem para ter um string de 'pedido' dentro do comando 'input()'
a=int(input('Entre com um valor: '))
b=int(input('Entre com um valor: '))
soma=a+b
subtracao=a-b
multiplicacao=a*b
divisao=a/b
resto=a%b
#É possivel utilizar concatenacao no 'print' usando o comando '.format', basta colocar '{}' onde devem ser colocadas as variasveis e ainda pode se usar um 'alias' (apelido) para as variaveis que vao ser inseridas no codigo
print('a soma é: {sum} \na subtracao é: {sub} \na multiplicacao é: {mult} \na divisao é: {divi} \no resto é: {res} '.
      format(sum=soma,sub=subtracao,mult=multiplicacao,divi=divisao,res=resto))
# print(type(soma))
# print('\na subtracao é: ' + str(subtracao))
# print(type(subtracao))
# print('\na mutiplicacao é: ' + str(multiplicacao))
# print(type(multiplicacao))
# print('\na divisao é: ' + str(divisao))
# print(type(divisao))
# print('\no resto da divisao é: ' + str(resto))
# print(type(resto))
# print('Teste de valor da soma do modo "format": {}'.format(soma))