#este programa demonstra listas
lista = [1,3,7,5]
lista_animal = ['cachorro','gato','elefante','lobo']
#para acessar uma posicao de algum objeto em uma lista é necessario usar '[]'
print(lista_animal[1])
for i in range(3):
    print(lista[i])
#o python possui o comando max e min para mostrar o maximo e o minimo de um arranjo de valores, respectivamente, para int e float ele ve qual o maior valor numerico e para str ele ve qual tem a maior letra inicial em ordem alfabetica
print('o maior valor da primeira lista é: {}'.format(max(lista)))
print('o menor valor da primeira lista é: {}'.format(min(lista)))
print(max(lista_animal))
#é possivel tambem verificar se existe algum valor na lista e caso nao exista é possivel usar o metodo 'append' que inclui algum valor na lista e o 'pop' remove a ultima entrada e o 'remove' remove uma entrada especifica
procura = str(input('Digite um animal: '))
if procura in lista_animal:
    print('existe "{}" na lista'.format(procura))
else:
    print('nao existe "{}" na lista. Será incluido(a)'.format(procura))
    lista_animal.append(procura)
    print(lista_animal)
#dá pra fazer operacoes com a lista ou com os valores dentro das listas tambem
lista[2]=lista[2]+500
lista += lista * 3
print(lista[2])
print(lista)