class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = Stack()
        self.stack_dequeue = Stack()
        self.size = 0

    def enqueue(self, item):
        # Para enfileirar um elemento, basta empurrá-lo para a pilha de enfileiramento
        self.stack_enqueue.push(item)
        self.size += 1

    def dequeue(self):
        if not self.stack_dequeue:
            # Se a pilha de desenfileiramento estiver vazia, transfira os elementos da pilha de enfileiramento para ela
            while self.stack_enqueue:
                self.stack_dequeue.push(self.stack_enqueue.pop())
        
        # Pop o elemento superior da pilha de desenfileiramento, que corresponde ao elemento mais antigo na fila
        if self.stack_dequeue:
            self.size -= 1
            return self.stack_dequeue.pop()
        else:
            # Se ambas as pilhas estiverem vazias, a fila está vazia
            return None

    def is_empty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def __len__(self):
        return self.size



































































# Exemplo de uso:
queue = QueueUsingStacks()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Tamanho da fila:", len(queue))  # Saída: 3

print("Dequeue:", queue.dequeue())  # Saída: 10



