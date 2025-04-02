# this question really has all the important things about heap,

import heapq
def reorganizeString(self, s: str) -> str:
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
        
    max_heap = [(-freq, char) for char, freq in freq_map.items()]
    heapq.heapify(max_heap)
    
    output =""
    
    while len(max_heap) >= 2:
        print(max_heap)

        freq1, char1 = heapq.heappop(max_heap)
        freq2, char2 = heapq.heappop(max_heap)
        
        output +=char1+char2
        print(output)
        # what if the prio is the same for two things, will it not pop same char and crash this logic
        # heap is orderd when the prio is the same, hence here the char1, char2 are not consecutive to each other
        
        if freq1 + 1 < 0:
            heapq.heappush(max_heap, (freq1 + 1, char1))
        if freq2 + 1 < 0:
            heapq.heappush(max_heap, (freq2 + 1, char2))
        print(max_heap)
        print("#")

    if max_heap:
        freq, char = heapq.heappop(max_heap)
        if -freq > 1:
            return ""
        output+=char
        
    return output