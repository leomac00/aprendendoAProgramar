#Coloca bullet points no começo de cada linha de uma lista
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
text = ''
for i in range(len(lines)):
    text += '* {}'.format(lines[i])


pyperclip.copy(text)