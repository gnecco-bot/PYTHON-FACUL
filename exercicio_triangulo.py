a = eval(input('Digite o lado: '))
b = eval(input('Digite o lado: '))
c = eval(input('Digite o lado: '))

maior_lado = max(a, b, c)

if maior_lado < a + b + c - maior_lado:
    print('Os lados formam um triângulo!')
    if a == b and b == a:
        print('Triângulo equilátero')
    elif a != b and b != c and a != c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Os lados não formam um triângulo')