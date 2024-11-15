class MinHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, valor):
        self.heap.append(valor)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, indice):
        while indice > 0 and self.heap[(indice - 1) // 2] > self.heap[indice]:
            self.heap[(indice - 1) // 2], self.heap[indice] = self.heap[indice], self.heap[(indice - 1) // 2]
            indice = (indice - 1) // 2

    def eliminar_min(self):
        if not self.heap:
            return None  # Si el heap está vacío, no hay nada que eliminar
        min_valor = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_valor

    def heapify_down(self, indice):
        while True:
            izquierda = 2 * indice + 1
            derecha = 2 * indice + 2
            menor = indice

            if izquierda < len(self.heap) and self.heap[izquierda] < self.heap[menor]:
                menor = izquierda
            if derecha < len(self.heap) and self.heap[derecha] < self.heap[menor]:
                menor = derecha
            if menor == indice:
                break
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            indice = menor

    def mostrar(self):
        print("MinHeap:", self.heap)


# Ejemplo solicitado del uso
min_heap = MinHeap()
min_heap.insertar(20)
min_heap.insertar(15)
min_heap.insertar(30)
min_heap.insertar(40)
min_heap.insertar(10)

min_heap.mostrar()

min_value = min_heap.eliminar_min()
print("Valor mínimo eliminado:", min_value)

min_heap.mostrar()