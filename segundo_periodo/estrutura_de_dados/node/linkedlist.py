from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # Método para inserir um elemento no final da lista
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Método para imprimir a lista
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Método para buscar um valor na lista
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    # Método para inserir um elemento em uma posição específica
    def insert(self, position, value):
        # Add na primeira posicao
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        count = 0
        while current_node and count < position - 1:
            current_node = current_node.next
            count += 1
        if current_node is None:
            print("Posição fora dos limites da lista.")
            return
        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node

    # Método para remover um elemento da lista
    def remove(self, value):
        current_node = self.head
        if current_node is not None:
            if current_node.data == value:
                self.head = current_node.next
                current_node = None
                return
        while current_node is not None:
            if current_node.data == value:
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node == None:
            print("O valor não está presente na lista.")
            return
        prev_node.next = current_node.next
        current_node = None

    # Método para contar o número de elementos na lista
    def count(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    

        


#lista = LinkedList() #cria a lista encadeada
#lista.append(2) # add um dado na lista
#lista.append(3) # add um dado na lista
#lista.append(4) # add um dado na lista
#lista.append(5) # add um dado na lista
#lista.print_list() # lista todos os dados
#print(lista.search(3)) #verifica se tem o dado
#lista.insert(3,6) # add na pocisao de sua escolha
#lista.print_list() # lista todos os dados

    
    