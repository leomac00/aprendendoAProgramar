#uma classe serve para agrupar um determinado algoritmo ou conjunto de metodos
class Calculadora:
    #para criar um metodo se utiliza a sintaxe abaixo, serve para nao ter que ficar repetindo codigo, dessa maneira posso criar um jeito mais conciso de repetir um algoritmo
    #o __init__ é um metodo que tem a caracteristica de sempre ser chamado assim que a classe é 'instanciada' (chamada no codigo)
    #self serve para referenciar o proprio metodo, basicamente serve para nao ter que ficar escrevendo o nome do metodo dentro dele mesmo toda hora (ate pq nem funciona pq existe o self para isso)
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def sub(self):
        return self.valor_a - self.valor_b
    def mult(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
a=int(input('Digite o valor "a": ' ))
b=int(input('Digite o valor "b": ' ))
calc=Calculadora(a, b)
print('a soma dos valores acima é: {}'.format(calc.soma()))
print('a subtracao dos valores acima é: {}'.format(calc.sub()))
print('a divisao dos valores acima é: {}'.format(calc.divisao()))
print('a multiplicacao dos valores acima é: {}'.format(calc.mult()))