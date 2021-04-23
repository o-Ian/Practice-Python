from math import cos,sin,tan,radians
angu = float(input('Digite um ângulo: '))
a = radians(angu)
print('O seno de {:.2f} é  {:.2f};\nO cosseno desse ângulo é {:.2f};\nA tangente é {:.2f}.' .format(angu, sin(a), cos(a), tan(a)))
