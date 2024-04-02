# O código a seguir exemplifica a implementação de pilhas usando arrays.
class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity  # Capacidade máxima da pilha
        self.stack = [None] * capacity  # Inicializa o array com capacidade definida
        self.top = -1  # Inicializa o índice do topo da pilha

    def is_empty(self):
        return self.top == -1  # Verifica se a pilha está vazia

    def is_full(self):
        return self.top == self.capacity - 1  # Verifica se a pilha está cheia

    def push(self, item):
        if self.is_full():
            print("Erro: Stack overflow")
        else:
            self.top += 1
            self.stack[self.top] = item  # Adiciona o elemento ao topo da pilha

    def pop(self):
        if self.is_empty():
            print("Erro: Stack underflow.")
            return None
        else:
            item = self.stack[self.top]  # Armazena o elemento do topo
            self.top -= 1  # Atualiza o topo para o próximo elemento
            return item

    def peek(self):
        if self.is_empty():
            print("Erro: Pilha vazia.")
            return None
        else:
            return self.stack[self.top]  # Retorna o elemento do topo da pilha

    def display(self):
        if self.is_empty():
            print("A pilha está vazia.")
        else:
            print("Elementos na pilha:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
