while True:
    nome = str(input('Quem é voce? '))
    if nome != 'leo':
        continue
    senha = str(input('Beleza, qual a senha? '))
    if senha == 'senha':
        break
print('voce é o bichao mesmo hein doido')
#########################################
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
#######################################
# while True:
#     nome = str(input('Digite seu nome: '))
#     if nome == 'seu nome':
#         print('Obrigado')
#         break
#######################################
# nome = None
# while nome != 'seu nome':
#     print('por favor digite seu nome')
#     nome = input()
# print('Obrigado')