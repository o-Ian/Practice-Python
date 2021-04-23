altura = float(input('Digite a sua altura em metro: '))
peso = float(input('Digite o seu peso em kg: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 25 >= imc >= 18.5:
    print('Você está no peso ideal!')
elif 30 >= imc > 25:
    print('Você está sobrepeso!')
elif 40 >= imc > 30:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')