# https://nostarch.com/contactus
import re, pyperclip
def getClipBoard():
    return str(pyperclip.paste())
def getRegex(type):
    regex = {
    'email' : re.compile(r'''(
    [a-zA-Z0-9._+-]+                # username
    @                               # @
    [a-zA-Z0-9]+                    # domain
    \.[a-zA-Z]+                     # .something
    )''',re.VERBOSE),
    'phone' : re.compile(r'''(
    (\+\d{2})?                      # country
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE),
    }
    return regex[type]
def getPhoneList():
        phoneList = []
        bufferList = getRegex('phone').findall(getClipBoard())
        for i in range(len(bufferList)):
            phoneList.append(bufferList[i][0])
        return phoneList
def getEmailList():
    return getRegex('email').findall(getClipBoard())

def getContacts():
    resultString = ''
    emailList = getEmailList()
    phoneList = getPhoneList()
    
    for i in range(len(emailList)):
        resultString += ('\n{}'.format(emailList[i]))
    resultString += '\n'
    for i in range(len(phoneList)):
        resultString += ('\n{}'.format(phoneList[i]))  

    print('\nThe following info was copied to your clipboard: \n {}'.format(resultString))
    return  pyperclip.copy(resultString)

getContacts()
