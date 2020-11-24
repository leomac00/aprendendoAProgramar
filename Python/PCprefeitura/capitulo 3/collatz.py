#esse se trata to projeto do capitulo 3 do livro automate boring stuff with python
def collatz(number):
     i=-1
     while number!=1 and i<501:
          i=i+1
          print('Repetição: '+str(i))
          if number % 2==0:
               number=number//2
               print('Resultado do Collatz():'+str(number))
          elif number % 2==1:
               number=number*3+1
               print('Resultado do Collatz():'+str(number))
#começa a roda o programa a partir daqui
print('Digite um numero inteiro')
num=int(input())
collatz(num)

