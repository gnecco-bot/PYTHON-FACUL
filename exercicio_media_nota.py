n1 = input('Digite a sua nota da diciplina: ')
n2 = input('Digite a sua outra nota da diciplina: ')
media = 0.4 * eval(n1) + 0.6 * eval(n2) 

if media >= 5:
    print('Você foi APROVADO!')
    print('Sua nota foi de 5 para cima! PARABÉNS!!!')
    print(f'Sua média foi de {media:.2f}')
else:
    print('Você foi REPROVADO!')
    print('Sua nota foi menor do que 5')
    print(f'Sua média foi de {media:.2f}') 