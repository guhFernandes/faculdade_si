from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Erro: Pilha vazia.")
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data

    def peek(self):
        if self.is_empty():
            print("Erro: Pilha vazia.")
            return None
        else:
            return self.top.data

    def display(self):
        current = self.top
        if self.is_empty():
            print("Pilha vazia.")
        else:
            print("Elementos na pilha:")
            while current is not None:
                print(current.data)
                current = current.next


def decimal_para_binario(data):
    # var list_binario virou um objeto da class Stack()
    list_binario = Stack()

    # Add o resto da divisao no top da pilha
    while data != 0:
        if data % 2 == 0:
            list_binario.push(0)
        else:
            list_binario.push(1)
        # Faco o dado receber ele msm dividido por dois recebendo o valor inteiro
        data //= 2
    
    binario = ''
    while list_binario.size != 0:
        # Trasformo o top em uma variavel str e removo ele do com o pop
        str_numb = str(list_binario.pop())
        # Concatena o top junto com a var binario para guardar o valor da conversao
        binario += str_numb 
    
    # Retorno a var binario para que possa ser manipolada 
    return binario
    
    

print(f'Binário -> {decimal_para_binario(36)}')
