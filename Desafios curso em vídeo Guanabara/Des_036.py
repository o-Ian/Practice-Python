valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário mensal? R$'))
qtd_ano = int(input('Em quantos anos você deseja pagar essa casa? '))
pres = valor/(qtd_ano*12)
if pres >= (0.3 * sal):
    print('O seu empréstimo foi \033[1;41mNEGADO\033[m!')
else:
    print('Parabéns, seu empréstimo foi \033[1;42mAPROVADO\033[m!')
