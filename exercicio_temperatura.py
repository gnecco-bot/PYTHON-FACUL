t = eval(input('Digite um temperatura: '))

def temperatura(t):
    if t >= 32 and t <= 86:
        print('Frio')
    elif t > 86:
        print('Quente!')
    else:
        print('Congelando')

temperatura(t)