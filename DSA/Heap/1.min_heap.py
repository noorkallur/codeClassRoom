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


    def remove_first(self):
        if not self.data:
            return None
        
        rm_val = self.data[0]

        self.data[0] = self.data.pop()
        end = len(self.data)
        
        index = 0
        print(self.data)
        while index < end:
            left_i= self.left(index)
            right_i= self.right(index)
            print(f"index:{index}, left:{left_i}, right:{right_i}")
            min_idx = -1
             
            if left_i >= end:
                break
            if right_i >= end:
                min_idx = left_i
            elif self.data[left_i] < self.data[right_i]:
                min_idx = left_i
            else:
                min_idx = right_i

            if self.data[index] < self.data[min_idx]:
                break

            self.data[index], self.data[min_idx] = self.data[min_idx], self.data[index]

            index = min_idx
    
        return rm_val

    def remove_at_index(self, index):
        end = len(self.data)
        if index > end -1:
            return None
        if index == end -1:
            self.data.pop()
            return
        
        self.data[index] = self.data.pop()
        end = end-1
        while index < end:
            left_i= self.left(index)
            right_i= self.right(index)
            min_idx = index

            print(f"index:{index}, left:{left_i}, right:{right_i}")
             
            if left_i < end and self.data[left_i] < self.data[min_idx]:
                min_idx = left_i

            if right_i < end and self.data[right_i] < self.data[min_idx]:
                min_idx = right_i

            if min_idx == index:
                break

            self.data[index], self.data[min_idx] = self.data[min_idx], self.data[index]

            index = min_idx
    

    def heapify_down(self, index):
        end = len(self.data)
        while index < end:
            left_i= self.left(index)
            right_i= self.right(index)
            min_idx = index

            print(f"index:{index}, left:{left_i}, right:{right_i}")
             
            if left_i < end and self.data[left_i] < self.data[min_idx]:
                min_idx = left_i

            if right_i < end and self.data[right_i] < self.data[min_idx]:
                min_idx = right_i

            if min_idx == index:
                break

            self.data[index], self.data[min_idx] = self.data[min_idx], self.data[index]

            index = min_idx
    
            
min_heap = Min_Heap()

min_heap.heapify(10)
min_heap.heapify(20)
min_heap.heapify(30)
min_heap.heapify(40)
min_heap.heapify(23)
min_heap.heapify(33)
min_heap.heapify(43)
min_heap.heapify(1)
print(min_heap.data)

min_heap.remove_at_index(0)
print(min_heap.data)

min_heap.remove_at_index(0)
print(min_heap.data)

min_heap.remove_at_index(0)
print(min_heap.data)