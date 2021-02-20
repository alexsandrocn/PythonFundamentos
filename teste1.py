def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split("\n")
    print(aluno_nota)
    for x in aluno_nota:
        print(x)


if __name__ == '__main__':
    media_notas('notas1.txt')
