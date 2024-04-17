# a = eval('2 * 3 + 1') VERDADEIRO
# print(a)
# a = eval('hello') FALSO
# print(a)
# a = eval("'hello' + 'not'+ 'world!'") VERDADEIRO
# print(a)
# a = eval("'ASCII'.count('I')") VERDADEIRO
# print(a)
# a = eval('x = 5') FALSO
# print(a)

# lista = ['Janeiro' , 'Fevereiro' , 'Março']
# for i in lista:
#     print(f'{i:.3}')

l = [3, 4, (2, 1)] 

l[2] = -1
l[0] = -1
print(l)
l[-1][0] = -1