lista=[5,2,5,3,7,89,1]
lista_animal=['arara','lobo','baleia','elefante','cachorro','papagaio']
#é possivel ordenar listas de acordo com um criterio usando o metodo '.sort'
lista.sort()
lista_animal.sort()
print(lista_animal)
print(lista)
#tuplas sao como listas mas nao podem ter seus valores alterados, voce cria uma tupla do mesmo jeito que uma lista porem usando () inves de []
tupla = (1,5,4,7,8)
print(tupla[3])
print('A tupla tem '+ str(len(tupla)) + ' elementos')
tupla_animal=tuple(lista_animal)
print(tupla_animal)