from node import Node

# O código a seguir implementa pilha com o uso de uma lista encadeada.
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

stack = Stack()

stack.push("Pão")
stack.push("Queijo")
stack.push("Presunto")

stack.display()

print("Elemento no topo da pilha:", stack.peek())

#Removendo os elementos da pilha
while not stack.is_empty():
    stack.pop()