# idade = eval(input('Digite sua idade: '))

# if idade > 62 :
    # print('Você pode obter benefícios de pensão')

# nomes = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
# nome = input('Digite seu nome: ')

# if nome in nomes:
#     print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

# defesa = eval(input('Digite um numero de defesa: '))
# golpe = eval(input('Digite um numero de golpe: '))

# if golpe > 10 and defesa <= 0:
#     print('Você está morto!')

# destino = input('Digite uma direção: ')
# l_destinos = ['norte', 'sul', 'leste', 'oeste']

# if destino.lower() in l_destinos:
#     print('Posso escapar')

# ano = eval(input('Digite um ano: '))

# if ano % 4 == 0:
#     print('Pode ser um ano bissexto.')
# else:
#     print('Definitivamente não é um ano bissexto.')

# usuario = input('Digite um usuario para o login: ')

# if usuario in ['joe', 'sue', ' hani', 'sophie' ]:
#     print('Login ', usuario)
#     print('Você entrou!')
#     print('Fim.')
# else:
#     print('Login', usuario)
#     print('Usuário desconhecido')
#     print('Fim.')

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

def meuIMC(altura, peso):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Normal')
    elif imc > 25:
        print('Acima do peso')

meuIMC(altura, peso)