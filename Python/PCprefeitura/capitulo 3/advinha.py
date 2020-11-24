#esse programa é um jogo de advinha
import random
nS=random.randint(1,20)
print('Tente advinhar o número que estou pensando, ele está entre 1 e 20!')
for tentativas in range(1,7):
     print('Chute um número')
     chute=int(input())
     if chute<nS:
         print('você chutou um número mais baixo do que o qual eu escolhi')
     elif chute>nS:
         print('você chutou um número mais alto que o número que escolhi.')
     else:
         break
if chute==nS:
     print('Parabéns, você é o bichão mesmo! acertou em '+str(tentativas)+' tentativas')
else:
     print('Você errrrrou! O número que escolhi foi '+str(nS)+'.')

