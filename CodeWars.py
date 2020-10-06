
  

###############################################

# #sum if given number if a multiple of 3 or 5
# def solution(number):
#     mult = []
#     for i in range (number):
#         if i % 3 == 0:
#             mult.append(i)
#         elif i % 5 == 0: 
#             mult.append(i)
#     return sum(mult)

# solution(10)
###############################################

# #Place all zeros to the end
# def move_zeros(array):
#     list = []
#     zeros = []
#
#     for i in range(len(array)):
#         if array[i] == 0 or array[i] == 0.0:
#             if type(array[i]) == int or type(array[i]) == float:
#                 zeros.append(array[i])
#             else:
#                 list.append(array[i])
#         else:
#             list.append(array[i])
#
#     return list + zeros
#
# print(move_zeros([1,2,False,1,0,1,0,3,0,1]))

###############################################
#
# def fibonacci(n):
#     soma = 1
#     ultimoCalculado = 1
#     penultimoCalculado = 0
#     i = 0
#     if n in [0,1,1]:
#         return n
#     for i in range (n-1):
#         soma = ultimoCalculado + penultimoCalculado
#         penultimoCalculado = ultimoCalculado
#         ultimoCalculado = soma
#     return soma
#
#
# print(fibonacci(50))
# print(str(12586269025) + '<= resultado para n = 50' )

#########################################

# #Criador de Hashtags, este programa cria hashtags a partir de uma frase digitada pelo usuario
# def generate_hashtag(frase):
#     if frase == '':
#         return False
#     if len(frase) > 140:
#         return False
#     else:
#         texto = ''
#         frase = frase.split(' ')
#         for palavra in frase:
#             texto += palavra.capitalize()
#         return '#' + texto
#
# print(generate_hashtag('oi eu        sou goku'))
#######################################

#Este programa verifica quais palavras de um array sao anagramas de uma palavra
# def anagrams(word, anagrams):
#     wordCount = {}
#     result = []
#     for character in word:
#         wordCount.setdefault(character, 0)
#         wordCount[character] += 1
#     for wordCheck in anagrams:
#         anagramCount = {}
#         for character in wordCheck:
#             anagramCount.setdefault(character, 0)
#             anagramCount[character] += 1
#         if anagramCount == wordCount:
#             result.append(wordCheck)
#         else:
#             pass
#     return result

################################################
# # this program returns a website domain name
# def domain_name(url):
#     from urllib.parse import urlparse
#     url = urlparse(url)
#     if len(url.netloc) > len(url.path):
#         url = url.netloc.split('.')
#         if url[0] == 'www':
#             url = url[1]
#         else:
#             url = url[0]
#     elif len(url.netloc) < len(url.path):
#         url = url.path.split('.')
#         if url[0] == 'www':
#             url = url[1]
#         else:
#             url = url[0]
#     return (url)
#
# domain_name("http://google.com")
# domain_name("http://google.co.jp")
# domain_name("www.xakep.ru")
# domain_name("https://youtube.com")
######################################
# # this program return the hex value for a given RGB value
# def rgb(r, g, b):
#     list = [r,g,b] #I turned the arguments into a list so I can use 'for' more easily
#     for index in range(len(list)):
#         if list[index] > 255: #the challenge says we have to round the number lower than 0 to 0 and greater than 255 to 255 so that's what we do here
#             list[index] = 255
#         elif list[index] < 0:
#             list[index] = 0
#         list[index] = hex(list[index]) #now we convert it to hex()
#         list[index] = list[index][2:].upper() #here we start formatting it to look like the result we want
#         if len(list[index]) == 1:
#             list[index] = '0' + list[index] #since the converted number might have just one valid digit we place one more zero at the front when it does
#     return (''.join(list))
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