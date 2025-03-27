# down_heap the non leaf nodes
# To go to non leaf node in a complete binary tree (no of nodes)//2


class Min_Heap:
 
    def left(self, index):
        return (index + 1) *2 -1
    
    def right(self, index):
        return (index +1)*2 
    
    def down_heap(self, index,  arr):
        left_idx = self.left(index)
        right_idx = self.right(index)
        min_index = index
        if left_idx < len(arr) and arr[left_idx] < arr[min_index]:
            min_index = left_idx

        if right_idx < len(arr) and arr[right_idx] < arr[min_index]:
            min_index = right_idx

        if min_index != index:
            #swap
            arr[index], arr[min_index] = arr[min_index], arr[index]
            self.down_heap(min_index, arr)

    def heapify(self, arr):
        n = len(arr)//2 -1

        while n >= 0:
            self.down_heap(n, arr)
            n -=1


arr = [10, 20 , 40 ,30, 1, 58, 34]
mh = Min_Heap()
mh.heapify(arr)
print(arr)