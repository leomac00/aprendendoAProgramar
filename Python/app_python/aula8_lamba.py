#funcao lambda é uma funcao anonima que tem por objetivo deixar o codigo mais conciso e rapido, a sintaxe utilizada é a que segue: *metodo* = lambda *parametro*: *o que ele vai fazer para entao retornar*; porem lambda só é eficiente em coisas que dao "para resolver em uma linha";
# é como se armazenase uma funcao em uma variavel
contador_letras = lambda lista: [len(x) for x in lista]
if __name__ == '__main__':
    lista_animais = ['cao','gato','baleia']
    print(contador_letras(lista_animais))
    calculadora = {
        'soma': lambda a, b: a + b,
        'subtracao': lambda a, b: a - b,
        'multiplicacao': lambda a, b: a * b,
        'divisao': lambda a, b: a / b
    }
    print(type(calculadora))
    #ao cirar um dicionario como no exemplo acima voce cria uma possibilidade de organizar um conjunto de funcoes em um só local, e criando um dicionario de funcoes anonimas fica mais facil para acessar determinadas funcoes

    #um dicionario serve para armazenar um conjunto de informacoes a partir de 'palavras chave' em uma variavel/metodo/funcao

    #na proxima linha eu estou basicamente dizendo que a variavel soma esta armazenando o valor respectivo ao texto 'soma' do dicionario *calculadora*
    soma = calculadora['soma']
    print('A soma é: {}'.format(soma(15,20)))