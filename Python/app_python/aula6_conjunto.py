conjunto = {1,2,3}
conjunto2 = {3,4,5,6}
print('Conjunto 1: {}'.format(conjunto))
print('COnjunto 2: {}'.format(conjunto2))
#é possivel unir e fazer a interseccao dos elementos de um conjunto
conjunto_uniao = conjunto.union(conjunto2)
conjunto_intesec = conjunto.intersection(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))
print('interseccao: {}'.format(conjunto_intesec))
#é possivel tambem fazer a diferenca entre conjuntos
conjunto_dif1 = conjunto.difference(conjunto2)
print('Diferenca do conjunto 1 para o 2: {}'.format(conjunto_dif1))
#porem neste caso a ordem dos fatores importam
conjunto_dif2 = conjunto2.difference(conjunto)
print('Diferenca do conjunto 2 para o 1: {}'.format(conjunto_dif2))
#tambem tem a diferenca simetrica que é basicamente a uniao das duas diferencas
conjunto_dif_sim = conjunto.symmetric_difference(conjunto2)
print('Diferenca Simetrica: {}'.format(conjunto_dif_sim))
#tem como verificar se um conjunto é um subset de um outro conjunto
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6}
print('Conjunto A: {}'.format(conjunto_a))
print('Conjunto B: {}'.format(conjunto_b))
conjunto_sub_a = conjunto_a.issubset(conjunto_b)
print('Conjunto A é subset do conjunto B? {}'.format(conjunto_sub_a))
conjunto_sub_b = conjunto_b.issubset(conjunto_a)
print('Conjunto B é subset do conjunto B? {}'.format(conjunto_sub_b))
# tem como verificar tambem se um conjunto é um superset do outro
conjunto_sup_b = conjunto_b.issuperset(conjunto_a)
print('Conjunto B é superSet do conjunto A? {}'.format(conjunto_sup_b))
# é possivel converter uma lista em um conjunto para remover as duplicatas
lista = ['cao','cao','gato','gato','elefante']
print('A lista de animais: {}'.format(lista))
conj_animais = set(lista)
lista_animais = list(conj_animais)
print('A lista que virou conjunto e agora nao possui duplicatas: {}'.format(conj_animais))
print('A convertendo o conjunto acima em lista... : {}'.format(lista_animais))
# conjunto = {1,5,2,3,4,5}
# #a diferenca de conjuntos para listas e tuplas é que em conjuntos n podem haver elementos repetidos
# print(str(conjunto) + str(type(conjunto)))
# conjunto.add(6)
# conjunto.discard(5)
# print(conjunto)