class Min_Heap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index + 1) //2 -1
    
    def left(self, index):
        return (index + 1) *2 -1
    
    def right(self, index):
        return (index +1)*2 
    

    def insert(self, val):
        self.data.append(val)
        self.up_heap(len(self.data)-1)
    
    def up_heap(self, index):
        if index == 0:
            return
        
        p_index = self.parent(index)
        if self.data[p_index] > self.data[index]:
            self.data[p_index], self.data[index] = self.data[index], self.data[p_index]
            self.up_heap(p_index)

    def remove_at_index(self, index):
        if index == len(self.data) -1:
            return self.data.pop()
            
        pop_val = self.data[index]
        self.data[index] = self.data.pop()

        self.down_heap(index)
        return pop_val

    def down_heap(self, index):
        left_idx = self.left(index)
        right_idx = self.left(index)
        min_index = index
        if left_idx < len(self.data) and self.data[left_idx] < self.data[min_index]:
            min_index = left_idx

        if right_idx < len(self.data) and self.data[right_idx] < self.data[min_index]:
            min_index = right_idx

        if min_index != index:
            #swap
            self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
            self.down_heap(min_index)

    def heap_sort(self):
        sorted_arr = []
        while len(self.data) > 0:
            sorted_arr.append(self.remove_at_index(0))
        return sorted_arr
    
min_heap = Min_Heap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(30)
min_heap.insert(1)
print(min_heap.data)
print(min_heap.heap_sort())
