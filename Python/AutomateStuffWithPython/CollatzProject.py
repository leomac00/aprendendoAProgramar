def collatz(number):
    if number % 2 == 0:
        numbero = number / 2
        print(numbero)
        return numbero
    else:
        numbero = number * 3 + 1
        print(numbero)
        return numbero
try:
    num = int(input("Digite um numero para comecar a sequencia de Collatz: "))
    colatiz = collatz(num)
    while colatiz != 1:
        colatiz = collatz(colatiz)

except ValueError:
    print("Digite um valor numerico inteiro.")