

#####################################
# #pyperclip demo
# import pyperclip
# pyperclip.copy('Olá Mundo!') #o que estiver como argumento será o texto enviado para a area de copia do usuario
# spam = pyperclip.paste() #a variavel 'spam' recebe o valor que está na area de copia do usuario
# print(spam)

###################################

# #Remove caracteres
# spam = '++++Olá mundo!++++'
# print(spam.strip('+'))
# print(spam.lstrip('+'))
# print(spam.rstrip('+'))
#
# spam = 'sabaooooooooooooo'
# print(spam.strip('o'))

##################################

# #Exemplos de justificacao de texto
# spam = 'Bolinha de Golfe'
# print(spam.ljust(25,'='))
# print(spam.rjust(25,'*'))
# print(spam.center(25,'+'))

##################################

# # split() e join()
# spam = 'Estou cansado de sempre ouvir Tarkus, porque demora tanto pra acabar?!'
#
# spam = spam.split()
# print(spam)
#
# spam = ' '.join(spam)
# print(spam)

##################################

# # starswith() e endswith()
# spam = 'Hello World!'
# print(spam.startswith('Bola'))
# print(spam.endswith('ld!'))

##################################

# # Exemplo de uso de método isX()
# while True:
#     idade = input('Digite sua idade: ')
#     if idade.isdecimal():
#         break
#     print('Digite um número para sua idade!')
# while True:
#     nome = input('Digite seu nome: ')
#     if nome.isalpha():
#         break
#     print('Digite um nome somente com letras!')
# print('Bem vindo {}'.format(nome))

########################################

# #Métodos isX()
#
# spam = 'Testando...'
# print(spam.isalpha())   #returns True if the string consists only of letters and is not blank.
#
# spam = '963852741 Tenho numeros também!'
# print(spam.isalnum())   #returns True if the string consists only of letters and numbers and is not blank.
#
# spam = '998855442211'
# print(spam.isdecimal())   #returns True if the string consists only of numeric characters and is not blank.
#
# spam = '    \n'
# print(spam.isspace())   #returns True if the string consists only of spaces, tabs, and newlines and is not blank.
#
# spam = 'Título'
# print(spam.istitle())   #returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

################################

# #upper() e lower()
# spam = 'Walk like an Egyption....'
#
# print(spam)
# spam = spam.lower()
# print(spam)
# spam = spam.upper()
# print(spam)

################################

# # In e Not In
# spam = 'Meu nome é Bleblio'
#
# print('Bleblio' in spam)
# print('é' not in spam)

################################

# # Indices em Strings
# spam = 'Hello World!'
#
# print('spam[1]: {}'.format(spam[1]))
# print('spam[3]: {}'.format(spam[3]))
# print('spam[-6]: {}'.format(spam[-6]))
#
# print('spam[1:6]: {}'.format(spam[1:6]))

###############################

# # Exemplo de simbolos e aspas triplas
# print(''''Para: Leo
# Bom dia, Leo.
# Hoje o dia será chuvoso,
# Um certo \'Alguém\' Baterá na sua porta, NÃO ATENDA!
# Assinado: Leo do futuro.
# ''')