class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest_index = index

        if left_index < len(self.heap) and self._compare(self.heap[left_index], self.heap[largest_index]):
            largest_index = left_index
        if right_index < len(self.heap) and self._compare(self.heap[right_index], self.heap[largest_index]):
            largest_index = right_index

        if largest_index != index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self._heapify_down(largest_index)

    def _compare(self, child, parent):
        return child > parent if self.max_heap else child < parent

# Пример использования
h = Heap(max_heap=True)

h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

while not h.is_empty():
    print("Извлеченный элемент:", h.extract())