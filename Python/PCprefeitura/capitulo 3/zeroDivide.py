def spam(dB):
    try:
        return 42 / dB
    except ZeroDivisionError:
        print('Erro: divisão por zero, argumento inválido.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
