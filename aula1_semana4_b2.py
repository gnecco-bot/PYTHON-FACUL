# Montagem PILHAS em python
# push() empilha(adiciona) o elemeno a pilha
# pop() desempilha(remove) o ultimo endereço armazenado e returna seu valor 
# top() apenas acessa o ultimo elemento da lista
# empty() verifica se está vazio
 
class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        
    def top(self):
        if len(self.data) > 0:
            return self.data(-1)
        
    def empty(self):
        return not len(self.data) > 0
    
p = Pilha()
print(p.push(4))
print(p.push(5))
print(p.push(6))
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop()) 

class Binario():
    def __init__(self, x):
        self.x = 2

# converte um numero decimal em binario
num = 31
while num > 0:
    resto = num % 2  # resto da divisão
    num = num // 2   # divisão sem valores com caças decimais
    p.push(resto)    # instancia o valor de resto na classe pilha adicionando a uma lista

while not p.empty(): # verifica se está vazio
    print(p.pop())   # exibe um por um dos valores de resto