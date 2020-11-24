

###################################

# #regex - pipe as second argument
# import re
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# text = '''foo'''


###################################

# #regex - re.VERBOSE
# import re
# phoneRegex1 = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# phoneRegex2 = re.compile(r'''(
# (\d{3}|\(\d{3}\))?              # area code
# (\s|-|\.)?                      # separator
# \d{3}                           # first 3 digits
# (\s|-|\.)                       # separator
# \d{4}                           # last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
# )''', re.VERBOSE)


###################################

# #regex - sub() method
# import re
# subRegex = re.compile(r'Agent \w+')
# text = 'Agent Alice turned the papers to Agent Bob last week'
# sub = subRegex.sub('CENSORED', text)
# print(sub) #CENSORED turned the papers to CENSORED last week

###################################

# #regex - matching anything
# import re 
# namesRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# text = 'First Name: Leonardo Last Name: Machado'
# mo = namesRegex.findall(text)
# print(mo) #[('Leonardo', 'Machado')]

###################################

# #regex - wildcard [.]
# import re
# wildcardRegex = re.compile(r'.at')
# mo = wildcardRegex.findall('The cat in the hat sat on the flat mat.')
# print(mo) #['cat', 'hat', 'sat', 'lat', 'mat']

###################################

# #regex - how to set beggining and ending of a strign
# import re

# begginingRegex = re.compile(r'^Hello')
# endingRegex = re.compile(r'\d$')

# text0 = 'Robocop is a bad movie'
# text1 = 'Hello world!'
# text2 = 'The correct answer is 42'

# mo01 =begginingRegex.findall(text0)
# mo02 = endingRegex.findall(text0)
# mo1 = begginingRegex.findall(text1)
# mo2 = endingRegex.findall(text2)

# print(mo01) #[]
# print(mo02) #[]
# print(mo1) #['Hello']
# print(mo2) #['2']

###################################

# # regex - character classes properties
# import re 
# consonantsRegex = re.compile(r'[^aeiouAEIOU ]')
# oneToFiveRegex = re.compile(r'[1-5]')

# text = 'Robocop likes to eat baby food at least 3 times per day'

# mo1 = consonantsRegex.findall(text)
# mo2 = oneToFiveRegex.findall(text)

# print(mo1)#['R', 'b', 'c', 'p', 'l', 'k', 's', 't', 't', 'b', 'b', 'y', 'f', 'd', 't', 'l', 's', 't', '3', 't', 'm', 's', 'p', 'r', 'd', 'y']
# print(mo2)#['3']

###################################

# # regex - making character classes
# import re
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# text = 'I like to write code in python because I can make cool stuff'
# mo = vowelRegex.findall(text)
# print(mo) #['I', 'i', 'e', 'o', 'i', 'e', 'o', 'e', 'i', 'o', 'e', 'a', 'u', 'e', 'I', 'a', 'a', 'e', 'o', 'o', 'u']

###################################

# #regex - xmas list using regex
# import re
# xmasRegex = re.compile(r'\d+\s\w+') 
# xmaslist = xmasRegex.findall('1 doll, 2 pens, 1 coal, 2 candy and 1 truck')
# print(xmaslist) #['1 doll', '2 pens', '1 coal', '2 candy', '1 truck']

###################################

# #regex - findall()
# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(type(mo)) #list
# print(mo) #['415-555-9999', '212-555-0000']

###################################

# #regex - greedy vs nongreedy
# import re
# greedyRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyRegex.search('HaHaHaHaHaHa')
# mo1.group()
# print(mo1)

# nonGreedyRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nonGreedyRegex.search('HaHaHaHaHaHa')
# mo2.group()
# print(mo2)

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