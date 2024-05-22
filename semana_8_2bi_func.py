# for : sempre começa na indice 0

def soma(arg):
    total = 1
    for i in arg:
        total += i
    return total

def mult(arg):
    total = 1
    for i in arg:
        print(i)
        total *= i 
    return total