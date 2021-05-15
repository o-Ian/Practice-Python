from titulo import *


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:

        return True

def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def mostrarArquivo(arq):
    a = open(nome, 'rt')
    for c in a:
        print(c)


def cadastro(arq, nome= '<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome:30}\t{idade} anos \n')
        except:
            print('Houve um erro ao adicionar o arquivo.')
        else:
            print('Dado cadastrado com sucesso!')
