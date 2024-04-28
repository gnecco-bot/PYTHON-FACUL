# FILA EM PYTHON
# inserir() insere um elemento no fim da fila
# remover() remover o primeiro elemento da fila
# empty() verifica se a fila está vazia
# top() retorna o valor da primeira posição da fila

class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)
    
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
    
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
   

f = Fila()
f.inserir(4)
f.inserir(2)
f.inserir(9)
f.inserir(12)
f.inserir(42)
print(f.remover())
print(f.remover())
print(f.remover())
print(f.empty())
print(f.top())