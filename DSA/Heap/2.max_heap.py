class Max_Heap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index + 1) //2 -1
    
    def heapify(self, val):
        self.data.append(val)

        index = len(self.data) - 1

        while index > 0:
            p_index = self.parent(index)

            if self.data[p_index] > self.data[index]:
                break

            self.data[p_index], self.data[index] = self.data[index], self.data[p_index] # swap

            index = p_index


max_heap = Max_Heap()

max_heap.heapify(10)
print(max_heap.data)

max_heap.heapify(3)
print(max_heap.data)

max_heap.heapify(5)
print(max_heap.data)

max_heap.heapify(7)
print(max_heap.data)

max_heap.heapify(2)
print(max_heap.data)

max_heap.heapify(20)
print(max_heap.data)

max_heap.heapify(21)
print(max_heap.data)