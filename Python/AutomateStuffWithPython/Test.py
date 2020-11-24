def foo (word):
    import pprint
    count = {}
    for c in word:
        count.setdefault(c, 0)
        count[c] += 1
    pprint.pprint(count)

foo('senhor dos aneis')

#############################################
# def fizzBuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(str(n))

# fizzBuzz(6)
#############################################
# spam = {'cat':1}
# print(spam['cat'])
# print(spam.values())
#############################################
# spam = {'bar': 100}
# print(spam['foo'])
#############################################
# def max_sequence(arr):
#     #My general idea is to check for each sub-array size inside the original arrray and each
#     #sequence for that given size which sum is the largest, if one sum is largest
#     #than the last one we log it into one variable and keep iterating it until all positions
#     #have been tested.
#     maxNumber = 0
#     for arraySize in range (len(arr)+1): # this sets the size of the array we are checking
#     #for the max number, it has to be from 0 up to arr+1 which is the maximum number of items
#     #inside the array because 0 might be maximum sum
#         for startingItem in range (0, len(arr)-arraySize+1): #it should start @ 0 and go up
#         #until the length of the array minus the test size plus 1
#             result = sum(arr[startingItem:(startingItem + arraySize)])
#             if result > maxNumber: #we assign the sum to a variable to check if i is bigger than the last sum
#                 maxNumber = result
#     return maxNumber
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) #if the code is right this should equal to six
# #spoiler: it is right
########################################
# def likes(names):
#   if len(names) == 0:
#     return 'no one likes this'
#   elif len(names) == 1:
#     names = ''.join(names)
#     return ('{} likes this'.format(names))
#   elif len(names) == 2:
#     names = ' and '.join(names)
#     return ('{} like this'.format(names))
#   elif len(names) == 3:
#     namesNew = ', '.join(names[:2])
#     ultimo = ''.join(names[2:])
#     return ('{} and {} like this'.format(namesNew, ultimo))
#   elif len(names) > 3:
#     namesNew = ', '.join(names[:2])
#     return ('{} and {} others like this'.format(namesNew, len(names)-2))
#
# array = ['ana','maria','joao']
# print(likes(array))
#####################################
# def longest(s1, s2):
#   newString = list(s1 + s2)
#   newString.sort()
#   unics = []
#   previous = None
#   for character in newString:
#     if character != previous:
#       unics.append(character)
#     previous = character
#   return ''.join(unics)
#####################################
# def unique_in_order(iterable):
#   unics = []
#   previous = None
#   for character in iterable:
#     if character != previous:
#       unics.append(character)
#     previous = character
#   return print(unics)
# unique_in_order('AAABBBCCCDF')
######################################
# def duplicate_encode(word):
#   newStr = ''
#   word = word.lower()
#   for i in range(len(word)):
#     count = word.count(word[i])
#     if count >= 2:
#       newStr += ')'
#     else:
#       newStr += '('
#   return newStr
#
# print(duplicate_encode('palavra'))
################################################
# def string_match(a, b):
#   count = 0
#   for i in range(max(len(a),len(b))):
#     if a[i-1:i] == b[i-1:i]:
#       count += 1
#   return count
################################################
# theArray = [['a','b','c'],['d','e','f'],['g','h','i']]
# zip(*theArray)

################################################
# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.index('cat'))
################################################
# spam = ["a","b","c","d"]
# print(spam[int(int('3' * 2) / 11)])
# print(spam[:2])
#################################################
#este programa testa possiveis erros ao acessar valores dentro de uma lista
# import random
# spam = 5
# lista = ["gato","rato"]
# try:
#     print(lista[spam])
# except TypeError:
#     print("erro no tipo do valor do argumento da lista, convertendo para int")
#     spam = int(round(spam))
# except IndexError:
#     spam = random.randint(0,len(lista)-1)
#     print("erro no indice da lista, acessando o indice aleatorio no. {} da lista".format(spam))
# finally:
#     print(lista[spam])
########################################
# def functionn():
#     pass
# print(type(functionn()))
########################################
#print(round(-12.59999))
#########################################
# spam = 1
# while spam <= 10:
#     print(spam)
#     spam += 1

##########################################
# for i in range (1, 11):
#     print(i)
##########################################
# spam = int(input('Type in a value: '))
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings')