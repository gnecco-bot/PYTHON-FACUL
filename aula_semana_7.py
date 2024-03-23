def simetrica(m):
    nlinhas = len(m)
    ncolunas = len(m[0])

    for i in range(nlinhas):
        # print('i do primeiro for', i)
        for j in range(i + 1, ncolunas):
            print("i do segundo for", i)
            print('j do segundo for', j)
            if m[i][j] != m[j][i]:
                print('entro no false')
                return False
            
    return print('é simetrica')

l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[1,2,3],[2,4,5],[3,5,3]]

# simetrica(l)
simetrica(l2)

for i in range(3):
    print(i)
    for l in range(3):
        print(l)