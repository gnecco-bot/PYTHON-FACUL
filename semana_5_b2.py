import random

# AULA 1
# Bubble sort
# faz ordenação de n elementos até sua ordem ser finalizada
# compara 2 valor cada vez que executa, um jogando 1 casa
# a esquerda ou direita, até que seja completo o algoritmo
# será necessario executar n vezes para implementar seus valores
# no lugar defenido (ordenação)
# cada rodada defini o ultimo valor, de traz para frente sucessivamente
# * range começa do 0 *  

def bubble_sort(v):
   for i in range(len(v)-1):
        # print(i,'= i')
        for j in range(len(v)-i-1):
            # print(j,'= jota')
            if(v[j] > v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]

v = [1,65,3,1,5,634,123,53]
print(v,'= bublle sort')
bubble_sort(v)
print(v,'= bublle sort')
print()

# Insertion sort
# guarda um valor na variavel
# um valor de inserção de deslocação por vez
# até sua posição adequada
# não precisa executar n vezes até seu valor chegar a indice 
# que necessaria, cada valor chega na indice predileta a cada rodada
# do algoritmo, fazendo uma ordenação do começo ao final sucessivamente 

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1
        while j >= 0 and x < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = x

l = [2,56,23,98,34,655,45,7]
print(l,'= insertion sort')
insertion_sort(l)
print(l,'= insertion sort')
print()

# AULA 2
# Merge sort
# trabalha como uma busca binaria
# divide a lista pela metade varias vezes até ficar 1
# compara os valores entre si e ordena 
# depois vai voltando recursivamente para as listas anteriores
# dividas, até que chegue ao final com toda a lista ordenada
     
def merge_sort(v, ini, fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)

def intercala(v, ini, meio, fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]
    L.append(999) #sentinela
    R.append(999) #sentinela
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1

vetor = [12,543,64,78,92,53,76,77,12]
print(vetor,'= merge_sort')
merge_sort(vetor, 0, len(vetor)-1)
print(vetor,'= merge_sort')
print()

# Quick sort
# dividir a lista em 2 partes
# ordenando da metade para esquerda e da metade para direita 
# pivo = é o valor do meio da lista usado como base
# para comparar valores e ordenar

def quick_sort(v, ini, fim):
    meio = (ini + fim) // 2
    pivo = v[meio]
    i = ini
    j = fim
    while i < j:
        while v[i] < pivo:
            i += 1
        while v[j] > pivo:
            j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    if j > ini:
        quick_sort(v, ini, j)
    if i < fim:
        quick_sort(v, i, fim)

lista = [25,33,56,54,11,35,12,43,57,23,67]
print(lista,'= quick sort')
quick_sort(lista, 0, len(lista)-1)
print(lista,'= quick sort')
print()

# AULA 3
# Heap sort
# cria uma arvore binaria na qual seu elemento de maior valor (raiz)
# é o topo da arvore, criando assim uma arvore heap_maximo
# valores maiores fica acima, valores menores a baixo
# elementos folhas de um vetor é lista / 2
# elementos não folhas é lista / 2 - 1
# exemplo [1, 2, 3, 4, 5, 6, 7, 8]
# do 1 ao 4 são elementos não folhas na qual tem filhos 
# do 5 ao 8 são elementos folhas, na qual não tem filhos

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heapify(arr, n, largest)
 
 
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at (n//2) we can start at that location.
 
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)
 
 
# Driver code to test above
 
arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
    print(arr[i])
print()

# AULA 4
# Buca Binária
# este tipo de busca funciona quando a lista esta odernada

def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio: # se o elemento não estiver na lista
        return -1

    if x == l[meio]: # elemento encontrado
        return meio
    
    if x < l[meio]: # caso elemento for menor, está ao lado esquerdo
        return busca_binaria(l, x, inicio, meio -1)

    if x > l[meio]: # caso elemento for maior, está ao lado direito
        return busca_binaria(l, x, meio + 1, fim)
    
# lista_random = random.sample(range(100), 20)
lista_random = [0, 10, 16, 48, 55, 56, 62, 67, 70, 76, 78, 86, 95]
print(lista_random)
lista_random.sort()
print(lista_random)
print(busca_binaria(lista_random, 56, 0, 19), '= valor do numero 56 na indice 5')

