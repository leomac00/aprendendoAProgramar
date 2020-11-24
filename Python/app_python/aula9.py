import shutil
def escrever_arquivo(texto):
    diretorio = 'C:/Users/Leonardo/Desktop/teste.txt' # é possivel tambem colocar o diretorio do arquivo para que ele seja salvo ou aberto por lá
    arquivo = open(diretorio,'w') # o Open cria um arquivo se ele n existir ou abre se ja existir
    arquivo.write(texto)            # o 'w' é para escrever em um arquivo
    arquivo.close()
def atualizar_arquivo(nome_arquivo, texto): # os parametros do metodo sao como variaveis utilizadas apenas dentro do metodo em si, servem para referenciar o que vai onde
    arquivo = open(nome_arquivo,'a')# o 'a' é para atualizar as informacoes d eum arquvio
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')# o 'r' serve para ler algum arquivo
    texto = arquivo.read()
    print(texto)
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        # lista_media.append(media(lista_notas))
        # print('O aluno {}obteve media {}.\n'.format(aluno , media(lista_notas)))
        lista_media.append('O aluno {}obteve media {}.\n'.format(aluno, media(lista_notas)))
    lista_media = ''.join(lista_media) #o .join usado dessa maneira serve para unir varios elementos de uma lista em um só string, é o modo reverso do split
    return lista_media
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Leonardo/Desktop/')
def move_arquvio(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Leonardo/Desktop/')
if __name__ == '__main__':
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda Linha.\n')
    # aluno = 'Eri Johnson , 1 , 6 , 10 , 9\n'
    # atualizar_arquivo('notas.txt',aluno)
    # ler_arquivo('teste.txt')
        # media = media_notas('notas.txt')
        # print(media)
        # atualizar_arquivo('medias_finais_dos_alunos.txt', media)
    #copia_arquivo('medias_finais_dos_alunos.txt')
    #move_arquvio('teste.txt')
    pass