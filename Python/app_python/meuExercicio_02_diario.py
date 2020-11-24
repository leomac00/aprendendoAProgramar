from aula9 import escrever_arquivo, atualizar_arquivo
if __name__ == '__main__':
    a = str(input('Digite a primeira entrada'))
    escrever_arquivo(a)
    a = str(input('Digite a entrada seguinte'))
    atualizar_arquivo('C:/Users/Leonardo/Desktop/teste.txt', a)
