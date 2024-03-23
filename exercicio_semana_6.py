def nfat(L):
    n = 0
    fat = 1
    while fat <= L:
        n += 1
        fat *= n
    return print(n-1)

nfat(119)
