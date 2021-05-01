from random import randint
x = randint(0, 10)
while True:
    while x < 5:
        x = randint(1, 10)
    if x >= 5:
        break

print(x)
