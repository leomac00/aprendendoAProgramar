

##########

# #getting Dir info
# import os

# path = 'C:\\Windows\\System32\\calc.exe'
# os.path.basename(path) #'calc.exe'
# os.path.dirname(path) #'C:\\Windows\\System32'
# os.path.split(path) #('C:\\Windows\\System32', 'calc.exe')

# calcPath = 'C:\\Windows\\System32\\calc.exe'
# calcPath.split(os.path.sep) #['C:', 'Windows', 'System32', 'calc.exe']

##########

# #Absolute and relative paths
# import os
# os.path.abspath('.\\') #c:/Users/Leonardo/Projects/Python/chapter8_files.py
# os.path.isabs('c:/Users/Leonardo/Projects/Python/chapter8_files.py') #True
# os.path.relpath('C:\\Users\\Leonardo\\Desktop') #'..\\..\\..\\..\\..\\Desktop'

##########

# #Creating directories
# import os
# os.makedirs('C:\\Users\\Leonardo\\Desktop\\test\\spam\\eggs\\foo')

##########

# # CWD -> Current Working Directory
# import os
# print(os.getcwd()) #C:\Users\Leonardo\Projects\Python
# #os.chdir('C:\\Users\\Leonardo\\thisPathDoesntExist') #FileNotFoundError
# os.chdir('C:\\Users\\Leonardo\\Desktop')
# print(os.getcwd()) #C:\Users\Leonardo\Desktop

##########

# #OS path example
# import os
# files = ['contacts.xls','welcome.txt','accounts.xls']
# for file in files:
#     print(os.path.join(r'C:\users\leonardo\documents', file))

#     #Prints:
#     # C:\users\leonardo\documents\contacts.xls
#     # C:\users\leonardo\documents\welcome.txt
#     # C:\users\leonardo\documents\accounts.xls    