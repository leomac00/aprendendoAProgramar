

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