class Tv:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        valor_canais = 1
    def power(self):
        if self.ligada: #nesses casos é possivel deixar com ou sem o == true porque se estiver sem nada o programa ja entende que eu estou querendo dizer que ele é igual a true
            self.ligada = False
        else:
            self.ligada = True
        print('A televisao está ligada? {}'.format(self.ligada))
    def aumenta_canal(self):
        valor_canais=int(input('Quantos canais deseja aumentar? '))
        self.canal += valor_canais
        print('A televisao está no canal: {}'.format(self.canal))
    def diminui_canal(self):
        valor_canais = int(input('Quantos canais deseja diminuir? '))
        self.canal -= valor_canais
        print('A televisao está no canal: {}'.format(self.canal))

print(__name__)
if __name__ == '__main__':
    #tem que colocar o if acima pois caso nao coloque o programa vai rodar o resto do codigo caso esteja sendo importado por algum outro modulo e as vezes isso pode nao ser interessante; basicamente o que o if __main__ == '__name__' esta dizendo é: se quem estiver me rodando tenha o nome do proprio arquivo execute o codigo a seguir, caso contrario n o faca
    televisao = Tv()
    print('A televisao está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('A televisao está no canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.diminui_canal()