# esse programa é um jogo de adivinhar o numero
import random
secretNumber = random.randint(1,21)
print(secretNumber)
for guessesTaken in range (1,7): # neste caso o jogo é para tentar adivinhar em menos de 6 tentativas.
    guess = int(input("Digite um numero: "))
    if guess > secretNumber: # essa condicao é ativada quando o numero é muito alto
        print("O numero é muito alto. tente outro")
    elif guess < secretNumber:# essa condicao é ativada quando o numero é muito baixo
        print("O numero é muito baixo. tente outro")
    else:# essa condicao é ativada quando o numero digitado é o correto, ou seja quando nao se encaixa em nenhuma das outras duas alternativas.
        break

if guess == secretNumber:
    print ("congratulaçoes, forasteiro! o numero {} é o correto!".format(guess))
else:
    print("infelizmente voce nao adivinhou o numero corretamente, meu camarada, o numero era o {}".format(guess))