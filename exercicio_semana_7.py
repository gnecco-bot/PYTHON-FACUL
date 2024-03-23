s = '0123456789'

print(s[2:5])
print(s[7:9])
print(s[1:8])
print(s[0:4])
print(s[7:])


previsao = 'It will be a sunny day today'

cont = previsao.count('day')
clima = previsao.find('sunny')
troca = previsao.replace('sunny', 'cloudy')

print(previsao)
print(f'cont {cont}, clima {clima}, troca {troca}.')


matrizNumeros = [ [ 1, 2, 3, 4 ], 
                [ 1, 3, 5, 7 ],
                [ 8, 6, 4, 2 ], 
                [ 7, 5, 3, 1 ] ] 

for i in range(len(matrizNumeros)):  
    for j in range(len(matrizNumeros[i])):  
        print(matrizNumeros[i][j], end=" ") 