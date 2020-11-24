from aula7_televisao import Tv
from aula7_calculadora2 import Calculadora
from aula8_contador_de_letras import contador_letras
if __name__ == '__main__':
    print('Aula 7: Televisao')
    televisao = Tv()
    televisao.power()
    televisao.aumenta_canal()
    print('-----------------------------------\nAula 7: Calculadora')
    calculadora = Calculadora()
    print(calculadora.sub(5, 2))
    print('-----------------------------------\nAula 8: Contador de letras de uma lista')
    print(contador_letras(['baleia','cao']))

