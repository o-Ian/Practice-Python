def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    print(f'Com {idade} anos: ', end='')
    if 18 < idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        return 'NÃO VOTA'
    else:
        return 'VOTO OPCIONAL'


anonasc = int(input('Qual o ano em que você nasceu? '))
print(voto(anonasc))
