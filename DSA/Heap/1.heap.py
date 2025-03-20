# heap

class Min_Heap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index) //2
    
    def left(self, index):
        return (index) * 2
    
    def right(self, index):
        return (index) * 2 + 1
    
    def insert_value(self, val):
        self.data.append(val)
        cur_index = len(self.data)    
        print(f"curr-{cur_index}")    
        while cur_index > 1:
            p_index = self.parent(cur_index) 
            print(f"{self.data[cur_index-1]}, {self.data[p_index-1]}")

            if self.data[cur_index-1] > self.data[p_index -1]:
                break
            self.data[cur_index - 1], self.data[p_index -1] = self.data[p_index -1], self.data[cur_index- 1] # swap
            print("swapped")
            print(self.data)
            cur_index = p_index
        

min_heap = Min_Heap()

min_heap.insert_value(10)
print(min_heap.data)

min_heap.insert_value(3)
print(min_heap.data)

min_heap.insert_value(5)
print(min_heap.data)

min_heap.insert_value(7)
print(min_heap.data)

min_heap.insert_value(2)
print(min_heap.data)

min_heap.insert_value(20)
print(min_heap.data)


min_heap.insert_value(18)
print(min_heap.data)

min_heap.insert_value(1)
print(min_heap.data)

min_heap.insert_value(11)
min_heap.insert_value(13)
print(min_heap.data)
min_heap.insert_value(14)
print(min_heap.data)
min_heap.insert_value(15)
print(min_heap.data)
