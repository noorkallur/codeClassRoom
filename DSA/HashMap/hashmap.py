# # Hash Map
# hash-maps are dict in python generally
# the core data structure of dict in python is Hash Table + Array
# this is ordered i.e. insertion order matters
# look up time is Average 0(1)


city_map = {}
city_map["USA"] = "New York" 
city_map["India"] ="Delhi"
canada_cities = ["Vancouver", "Winnipeg"]
# city_map["canada"].append(canada_cities) #canada not initiallized
city_map["Canada"] = canada_cities # initialization

print(city_map)

# Hash Map (Dictionary) Methods
# dict.get(key[, default]): Returns the value for key if key is in the dictionary, else default.
# dict.keys(): Returns a view object displaying a list of all the keys in the dictionary.
# dict.values(): Returns a view object displaying a list of all the values in the dictionary.
# dict.items(): Returns a view object displaying a list of dictionary's key-value tuple pairs.
# dict.update([other]): Updates the dictionary with the key-value pairs from other, overwriting existing keys.
# dict.pop(key[, default]): Removes the specified key and returns the corresponding value. If the key is not found, default is returned.
# dict.popitem(): Removes and returns a key-value pair as a tuple. Pairs are returned in LIFO (last-in, first-out) order.
# dict.clear(): Removes all items from the dictionary.
# dict.setdefault(key[, default]): Returns the value for key if key is in the dictionary; if not, inserts key with a value of default and returns default.

# city_map["Japan"] # keyError
print(city_map.get("Japan")) # returns None

# dict are orderd hash_maps, hence when you popitem(). its going to pop the last entered key-value pair
city_map.popitem() 
print(city_map)

# iterating thru hashmap
for key, value in city_map.items():
    print(f"{key}, {value}")

# getting value, if not present return default
print(city_map.get('India', "NA"))
print(city_map.get('Japan', "NA"))


# # diff b/w dict and defaultdict
# # dict: Raises KeyError for missing keys.
# # defaultdict: Provides a default value for missing keys.
# # Since defaultdict is a subclass of dict, it inherits all the methods of a dictionary. 
from collections import defaultdict

#default dict will make the entries None
city_map = defaultdict(list)
city_map["USA"] = "New York" # normal way
city_map["India"].append("Delhi")# you can append like this too

print(city_map)
print(city_map["India"]) # return ['Delhi']
print(city_map["Japan"]) # returns []
print(city_map.get("Japan")) # returns []



# # Hash Set
# # 1. No duplicate elements. If try to insert the same item again, it overwrites previous one.
# # 2. An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
# # Sets are used in various scenarios where you need to store unique elements and perform operations like membership tests, union, intersection, and difference efficiently. 
hs = set([1, 2, 3, 4, 4, 1])
print(hs)

# print(hs[0]) # cant do this

# # Hash Set Methods
# # set.add(elem): Adds an element to the set.
# # set.remove(elem): Removes an element from the set. Raises KeyError if the element is not found.
# # set.discard(elem): Removes an element from the set if it is present.
# # set.pop(): Removes and returns an arbitrary(unspecified) set element. Raises KeyError if the set is empty.
# # set.clear(): Removes all elements from the set.
# # set.union(*others): Returns a new set with elements from the set and all others.
# # set.intersection(*others): Returns a new set with elements common to the set and all others.
# # set.difference(*others): Returns a new set with elements in the set that are not in the others.
# # set.symmetric_difference(other): Returns a new set with elements in either the set or other but not both.
# # set.update(*others): Updates the set, adding elements from all others.
# # set.intersection_update(*others): Updates the set, keeping only elements found in it and all others.
# # set.difference_update(*others): Updates the set, removing elements found in others.
# # set.symmetric_difference_update(other): Updates the set, keeping only elements found in either the set or other but not both.

# # check whetehr item is present in set or not 
print(1 in hs)