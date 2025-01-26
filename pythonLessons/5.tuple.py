# # lets first understand the differnce beteween the LIST and TUPLE
# # Sno         LIST                                                                    TUPLE

# # 1	Lists are mutable	                                                            Tuples are immutable
# # 2	The implication of iterations is Time-consuming	                                The implication of iterations is comparatively Faster
# # 3	The list is better for performing operations, such as insertion and deletion.	A Tuple data type is appropriate for accessing the elements
# # 4	Lists consume more memory	                                                    Tuple consumes less memory as compared to the list
# # 5	Lists have several built-in methods	                                            Tuple does not have many built-in methods.
# # 6	Unexpected changes and errors are more likely to occur	                        In a tuple, it is hard to take place.

# # TUPLE:
# # A tuple in Python is a collection of ordered and immutable objects. Tuples are similar to lists, but they cannot be changed once they are created.
# # This makes them useful for storing data that should not be modified, such as database records.

# # to create a tuple use () and once initiated cannot be changed 

player_coordinates = (1 , 2, 3, 4, "NA")
print(player_coordinates[0])
# # player_coordinates[0] = 99 // doesn't support assignment
x, y, z, *others = player_coordinates
print(f'{x}, {y}, {z}, {others}')
