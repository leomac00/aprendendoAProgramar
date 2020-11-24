class Error(Exception): #sempre que quiser ter uma classe de excecao tem que ter essa calsse error mesmo que ela n faca nada para que ela puxe de Exception
    pass
class InputError(Error): #por convencao toda classe que trata erro deve terminar em Error
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x > 10:
            raise InputError('Digite um valor menor que 10')
        elif x < 0:
            raise InputError('Digite um valor maior que 0')
        print('Nota: {}'.format(x))
        break
    except InputError as ex:
        print(ex)
    except ValueError:
        print('Digite apenas numeros')
