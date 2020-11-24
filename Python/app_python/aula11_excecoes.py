lista = [1, 10]
arquivo = open('notas.txt', 'r')
try:
    texto = arquivo.read()
    numero = lista[1]
    print(numero)
    divisao = 10/0
    a = 1
    x = a
#a ordem dos exceptions deve respeitar a ordem da arvore dos erros que esta na documentacao dos exceptions do python pois caso voce coloque um except que eta acima primeiro ele vai tratar todos os erros susequentes como sendo daquele tipo "maior" na arvore.
except ZeroDivisionError:
    print('houve um erro ao tentar dividir por zero')
except ArithmeticError: #faz com que erros especifico no programa se manifestem de uma determinada maneira desejada
    print('Houv um erro ao realizar uma operacao aritimetica')
except IndexError:
    print('erro ao acessar um indice invalido da lista')
except BaseException as ex: # o BaseException é o erro como ele é, ao fazer o codigo anterior voce mostra o erro em si como a variavel 'ex' e entao printa ele para qu se conheca o erro no codigo. todo erro é primeiramente do BaseException
    print('Erro desconhecido: {}'.format(ex))
# except: # é usado para erros genericos
#     pass
else: # posso usar o else aqui para executar um codigo quando n ocorrer nenhum erro no bloco try
    print('executa quando n ocorre nenhuma excecao')
finally:
    print('sempre executa')
    print('Fechadno arquivo')
    arquivo.close()