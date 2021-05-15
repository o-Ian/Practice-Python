import titulo
import VerificaErros
import arquivo
from time import sleep

arq = 'cadastro.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    titulo.titulo('MENU PRINCIPAL')
    print('[1] - Ver pessoas cadastradas')
    print('[2] - Cadastrar nova pessoa')
    print('[3] - Sair do Sistema')
    print('-'*35)
    opcao = VerificaErros.leiaInt('Sua opção: ')
    while opcao != 3 and opcao != 2 and opcao != 1:
        print('\033[1;31mERRO! Digite um número válido.\033[m')
        opcao = VerificaErros.leiaInt('Sua opção: ')
    if opcao == 1:
        arquivo.lerArquivo(arq)
    elif opcao == 2:
        titulo.titulo('CADASTRO DE PESSOA')
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        arquivo.cadastro(arq, nome, idade)
    elif opcao == 3:
        print('\033[1mSAINDO DO PROGRAMA.... até logo!\033[m')
        break

