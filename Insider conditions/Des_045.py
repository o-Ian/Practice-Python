from random import randint
from time import sleep
print('\033[36m-=\033[m'*20)
print('\033[1;33mVOCÊ CONSEGUE GANHAR?\033[m')
print('\033[36m-=\033[m'*20)
eu = input('\033[1;40mDigite pedra, papel ou tesoura.\033[m ') .strip().lower()
pc = randint(1, 3)
if pc == 1:
    pc = 'pedra'
elif pc == 2:
    pc = 'papel'
elif pc == 3:
    pc = 'tesoura'
else:
    print('\033[41mDigite pedra, papel ou tesoura!\033[m')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
ganhei = 'Você jogou {} e eu {}.\nAAAARGGH, VOCÊ VENCEU!' .format(eu, pc)
perdi = 'Eu joguei {} e você {}.\nEU GANHEI, HAHAHAHA!' .format(pc, eu)
empate = 'Eu joguei {} e você {}.\nEMPATAMOS, TENTE NOVAMENTE!' .format(pc, eu)

if eu == pc:
    print(empate)
elif eu == 'pedra' and pc == 'tesoura':
    print(ganhei)
elif eu == 'papel' and pc == 'pedra':
    print(ganhei)
elif eu == 'tesoura' and pc == 'papel':
    print(ganhei)
else:
    print(perdi)
