###################################

# #regex - curly brackets [{}]
# import re 
# haRegex_strict3 = re.compile(r'(Ha){3}') #match strictly 3 times 'Ha'
# haRegex_3to5 = re.compile(r'(Ha){3,5}') #match between 3 and 5 times 'Ha'
# haRegex_min3 = re.compile(r'(Ha){3,}') #match at least 3 times 'Ha'
# haRegex_max5 = re.compile(r'(Ha){,5}') #match at max 5 times 'Ha'

# mo_strict3 = haRegex_strict3.search('HaHaHaHaHaHa') 
# mo_3to5 = haRegex_3to5.search('HaHaHaHaHaHa') 
# mo_min3 = haRegex_min3.search('HaHaHaHaHaHa') 
# mo_max5 = haRegex_max5.search('HaHaHaHaHaHa') 

# print(mo_strict3.group()) #HaHaHa (3 times)
# print(mo_3to5.group()) #HaHaHaHaHa (5 times)
# print(mo_min3.group()) #HaHaHaHaHaHa (6 times)
# print(mo_max5.group()) #HaHaHaHaHa (5 times)

###################################

# #regex - plus sign [+]
# import re
# batRegex = re.compile(r'Bat(wo)+man')
# mo_1 = batRegex.search('The adventures of Batwowowoman')
# mo_2 = batRegex.search('The adventures of Batman')

# print(mo_1.group()) #Batwowowoman
# print(mo_2 == None) #True

###################################

# #regex - asterisk [*]
# import re
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The adventures of Batwowowowowowowoman')

# print(mo.group()) #Batwowowowowowowoman

###################################

# #regex - question mark [?]
# import re
# batRegex = re.compile(r'Bat(wo)?man') #re.compile para o padrao que estou buscando
# mo = batRegex.search('Look! it\'s the Batwoman!') #variavel.seacrh('texto')|findall('texto') para enconstrar no texto o padrao compilado 

# print(mo.group()) #Batwoman

###################################

# #regex - pipe [|]
# import re
# batRegex = re.compile(r'(Bat|bat)(man|mobile|copter|tery)')
# mo = batRegex.findall('Look! Batman just got off the batcopter and it\'s entering the batmobile but he doesn\'t know it\'s out of battery!')

# print(mo) #[('Bat', 'man'), ('bat', 'copter'), ('bat', 'mobile'), ('bat', 'tery')]

###################################

# #regex - groups()
# import re
# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #separam-se os grupos utilizando parenteses
# mo = phoneNumberRegex.search('415-555-4242 is a phone number') #cria-se o MO

# areaCode, mainNumber = mo.groups()

# print('Tuple (mo.groups()): {}'.format(mo.groups())) #('415', '555-4242')
# print('Area code (group 1): ' + areaCode)
# print('Main number (group 2): ' + mainNumber)


###################################

# #regex - group()
# import re
# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #separam-se os grupos utilizando parenteses
# mo = phoneNumberRegex.search('415-555-4242 is a phone number') #criando o MO

# print(mo.group(1)) #415
# print(mo.group(2)) #555-4242
# print(mo.group( )) #415-555-4242

###################################

# # Find phone number with Regex
# import re #importando

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #objeto regex
#                           #^ 'r' serve para a strign que segue nao utilizar escape characters
# spam = phoneNumRegex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
# print(spam) # ['415-555-1011', '415-555-9999']

###################################

# # Find phone number without Regex
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True    

# def findPN(text):
#     for i in range(len(text)):
#         chunk = text[i:i+12]
#         if isPhoneNumber(chunk):
#             print('Number found: {}'.format(chunk))

# # print('415-555-4242 is a phone number:')
# # print(isPhoneNumber('415-555-4242')) #True
# # print('Moshi moshi is a phone number:')
# # print(isPhoneNumber('Moshi moshi')) #False

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# findPN(message)