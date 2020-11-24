import re
def getRegex(type):
    regex = {
        'AtoZ' : re.compile(r'[A-Z]+'),
        'atoz' : re.compile(r'[a-z]+'),
        '0to9' : re.compile(r'[0-9]+'),
        'SpCh'   : re.compile(r'[@#$%^&+=]+'),
    }
    return regex[type]
def testPW(password):
    if  len(getRegex('AtoZ').findall(password)) > 0 and len(getRegex('atoz').findall(password)) > 0 and len(getRegex('0to9').findall(password)) > 0 and len(getRegex('SpCh').findall(password)) > 0:
        return print('good password')
    else:
        return print('bad password')
def regexStrip(text, character = r'^\s'):
    regex = re.compile(character)
    return print(regex.sub('', text))

regexStrip(' oi eu sou goku ')