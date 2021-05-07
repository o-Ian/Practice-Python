def area(l, c):
    area = int(l*c)
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area}m².')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
