class Calculadora:
    #para criar um metodo se utiliza a sintaxe abaixo, serve para nao ter que ficar repetindo codigo, dessa maneira posso criar um jeito mais conciso de repetir um algoritmo
    #o __init__ é um metodo que tem a caracteristica de sempre ser chamado assim que a classe é 'instanciada' (chamada no codigo)
    #self serve para referenciar o proprio metodo, basicamente serve para nao ter que ficar escrevendo o nome do metodo dentro dele mesmo toda hora (ate pq nem funciona pq existe o self para isso)
    def __init__(self):
        pass
    def soma(self, valor_a, valor_b): #ainda sobre o self, neste exemplo,ele serve entao basicamente pra dizer 'para me chamar voce precisa digitar: 1. o nome do metodo (soma); 2. o argumento valor_a; 3. o argumento valor_b'; da seguinte maneira: soma(valor_a, valor_b)
        return valor_a + valor_b
    def sub(self, valor_a, valor_b):
        return valor_a - valor_b
    def mult(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
print(__name__)
if __name__ == '__main__':
    a=int(input('Digite o valor "a": ' ))
    b=int(input('Digite o valor "b": ' ))
    calc=Calculadora()
    print('a soma dos valores acima é: {}'.format(calc.soma(a, b)))
    print('a subtracao dos valores acima é: {}'.format(calc.sub(a, b)))
    print('a divisao dos valores acima é: {}'.format(calc.divisao(a, b)))
    print('a multiplicacao dos valores acima é: {}'.format(calc.mult(a, b)))
    # a grande diferenca desse programa para o anterior é que inves de declrar os argumentos para as contas serem feitas logo no inicio quando chamavamos a classe Calculadora() agora devem ser exigidos posteiormente e individualmente para cada metodo