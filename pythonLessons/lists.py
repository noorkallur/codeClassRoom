# List : ordered, mutable, and heterogeneous collection of objects.
# these objects are written within square brackets [ ]. this is how we identify if its a list or not.

# # lists:
# # lists are built into python, so you don’t need to import any module to use them.
# # lists can contain items of multiple data types, such as integers, strings, and even other lists.
# # accessing an element in a list is fast as elements are stored in contiguous memory locations.
# # inserting or deleting elements at the beginning or in the middle of a list can be inefficient due to the need to shift subsequent elements linearly.

# # w.a.p to find the largest number in a list
# list = [12, 5, 7, 8, 37, 56]
# max = list[0]
# for item in list:
#     if(item > max):
#         max = item
# print(f"larges number: {max}")

## 2D list 
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)
# for row in matrix:
#     for item in row:
#         print(item)

## List methods https://docs.python.org/3/tutorial/datastructures.html
# # Method	    Description
# # append()	Adds an element at the end of the list
# # clear()	    Removes all the elements from the list
# # copy()	    Returns a copy of the list
# # count()	    Returns the number of elements with the specified value
# # extend()	Add the elements of a list (or any iterable), to the end of the current list
# # index()	    Returns the index of the first element with the specified value
# # insert()	Adds an element at the specified position
# # pop()	    Removes the element at the specified position
# # remove()	Removes the first item with the specified value
# # reverse()	Reverses the order of the list
# # sort()	    Sorts the list

##list.copy() -> Return a shallow copy of the list. Equivalent to a[:].
## what does the above statement mean??
## https://realpython.com/copying-python-objects/
##A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original.
##In essence, a shallow copy is only one level deep. The copying process does not recurse and therefore won’t create copies of the child objects themselves.

# #A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original.
# #Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children
## Example is given below
# # first we have to understand that shallow copy only copes one  level deep i.e if a list contains mutable (list) and immuatble(int) objects and lets say we shallow copy it, 
# # immutable objects have their own memory when created(refer above) and it does not matter if its shallow or deep copy for immutable objects 
# # BUTTT FOR mutable objects it matters, if we shallow copy it only copies the address to the copy list but the data deep in it.

# list1 = [1, 2, 3]
# list2 = list1.copy()
# print(f"id1 - {id(list1)}")
# print(f"id2 - {id(list2)}") # both the ids are diffrent

# list1[0] = 34

# print(f"id2 - {id(list2)}")
# print(f"id1 - {id(list1)}")
# print(list1)
# print(list2)



# original_list = [[1, 2, 3], [4, 5, 6], 56]

# shallow_copy = original_list.copy()
# print(f"id01 - {id(original_list)}")
# print(f"ids2 - {id(shallow_copy)}") # both the ids are diffrent 
# shallow_copy[1][0] = 99 # since the both copies point to the same reference, its going to change for both 
# shallow_copy[2] = 1000 # its only goin to change in one copy

# print("Original List:", original_list) # [[1, 2, 3], [99, 5, 6], 56]
# print("Shallow Copy:", shallow_copy)   # [[1, 2, 3], [99, 5, 6], 1000]

# print(f"id01 - {id(original_list)}")
# print(f"ids2 - {id(shallow_copy)}")
# print(original_list)
# print(shallow_copy)
# print(56 in original_list)

# import copy

# # Original list of lists
# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Deep copy the list
# copied_list = copy.deepcopy(original_list)

# # Verify the copy
# print("Original List:", original_list)
# print("Copied List:", copied_list)


# # wap to remove the duplicates in a list
# import time

# def my_operation():
#     list = [1, 2, 3, 4, 5, 2, 7]
#     removeList = []
#     for idx, item in enumerate(list):
#         if(idx < len(list) -1 and item in list[idx +1:]):
#             removeList.append(item)
#     for ritem in removeList:
#         list.remove(ritem)
#     print(list)
# pass
# def tutor_operation():
#     list = [1, 2, 3, 4, 5, 2, 7]
#     uniques = []
#     for item in list:
#         if item not in uniques:
#             uniques.append(item)
#     print(uniques)
# pass
# start_time = time.time()
# my_operation()
# end_time = time.time()

# print(f"Time taken to perform my_operation: {(end_time - start_time)} ms")
# start_time = time.time()
# tutor_operation()
# end_time = time.time()

# print(f"Time taken to perform tutor_operation: {(end_time - start_time)} ms")


# # List comprehension
numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5, 6]
even_odd = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(even_odd)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_a)  # Output: ['apple', 'banana', 'mango']

# combining two lists into one 
a = [1, 2, 3]
b = ['a', 'b', 'c']

combined = [(a[i], b[i]) for i in range(len(a))]
print(combined)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# using zip
a = [1, 2, 3]
b = ['a', 'b', 'c']

combined = list(zip(a, b))
print(combined)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# adding two lists elements into one list
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 0, 567, 7, 8]
newlist = [x + y for x, y in zip(nums1, nums2)] #zip exhausts till the shortest lists and also it returns tuple by default
print(newlist)

new_list = [(x, y) for x in [1,2,3,5] for y in [3,1,4,5] if x != y]
