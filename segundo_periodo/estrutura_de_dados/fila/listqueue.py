class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3 # Capacidade da fila

    def enqueue (self, data):
      if self.size == self.rear:
        print("Fila está cheia \n")
      else:
        self.items.append(data)
        self.rear += 1

    def dequeue(self):
      if self.front == self.rear:
        print("Fila está vazia")
      else:
        data = self.items.pop(0) # exclui o item da extremidade inicial da fila
        self.rear -= 1
        return data