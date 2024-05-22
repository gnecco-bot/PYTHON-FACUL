# Testes automatizados para verificação de valores de entrada
# __name__ : significa mencionando o arquivo que esta sendo executado

from semana_8_2bi_func import soma, mult

def test_soma():
    assert soma([1, 2, 3]) == 6, 'Deve ser 6'

def test_mult():
    assert mult((2, 3, 4)) == 24, 'Deve ser 24'

if __name__ == '__main__':
    test_soma()
    test_mult()
    print('Tudo ok!')
