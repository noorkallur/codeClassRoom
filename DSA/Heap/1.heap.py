class Min_Heap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index + 1) //2 -1
    
    def left(self, index):
        return (index + 1) *2 -1
    
    def right(self, index):
        return (index +1)*2 
    
    def heapify(self, val):
        self.data.append(val)

        index = len(self.data) -1

        while index > 0:
            p_index = self.parent(index)
            if self.data[p_index] < self.data[index]:
                break
            
            self.data[p_index], self.data[index] = self.data[index], self.data[p_index] # swap

            index = p_index

    
min_heap = Min_Heap()

min_heap.heapify(10)
print(min_heap.data)

min_heap.heapify(3)
print(min_heap.data)

min_heap.heapify(5)
print(min_heap.data)

min_heap.heapify(7)
print(min_heap.data)

min_heap.heapify(2)
print(min_heap.data)

min_heap.heapify(20)
print(min_heap.data)


min_heap.heapify(18)
print(min_heap.data)

min_heap.heapify(1)
print(min_heap.data)

min_heap.heapify(11)
min_heap.heapify(13)
print(min_heap.data)
min_heap.heapify(14)
print(min_heap.data)
min_heap.heapify(15)
print(min_heap.data)
