# # Heap in python lib, use import heapq
# # heapq module in Python implements a min-heap by default. This means that the smallest element is always at the root of the heap

# # Methods
# # heapq.heappush(heap, item): Pushes the value item onto the heap, maintaining the heap invariant.
# # heapq.heappop(heap): Pops and returns the smallest item from the heap, maintaining the heap invariant.
# # heapq.heappushpop(heap, item): Pushes item onto the heap, then pops and returns the smallest item.
# # heapq.heapify(x): Transforms the list x into a heap, in-place, in linear time.
# # heapq.heapreplace(heap, item): Pops and returns the smallest item from the heap, and pushes the new item.
# # heapq.nlargest(n, iterable, key=None): Returns a list with the n largest elements from the dataset defined by iterable.
# # heapq.nsmallest(n, iterable, key=None): Returns a list with the n smallest elements from the dataset defined by iterable.
# # heapq.merge(*iterables, key=None, reverse=False): Merges multiple sorted inputs into a single sorted output, returning an iterator.
# # heapq._heapify_max(x): Transforms the list x into a max-heap, in-place (not part of the public API).
# # heapq._heappop_max(heap): Pops and returns the largest item from the heap (not part of the public API).
# # heapq._heapreplace_max(heap, item): Pops and returns the largest item from the heap, and pushes the new item (not part of the public API).

# # NOTE: _heapify_max is not recommended as its private function, it might change in future

# # to make a maxheap use negation of the heap


# # import note
# The heapq module in Python provides functions for creating and managing heaps. By default, it implements a min-heap, where the smallest element is at the root.

# Behavior with Lists of Pairs
# When working with lists of pairs, the heapq module uses the default comparison operator to organize the heap. The comparison works as follows:

# First Element: It compares the first elements of the pairs.
# Second Element: If the first elements are equal, it then compares the second elements.