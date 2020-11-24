#Esse erro ocorre ao tentar dividr por zero.
def spam (divideBy):
    return 42 / divideBy
try:
    print(spam(10))
    print(spam(64))
    print(spam(0))
    print(spam(42))
except ZeroDivisionError:
    print("Argumento da funcao invalido. digite outro valor.")