# creating a trie using a hashmap
# TRIE Node structure
class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

# TRIE class
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            #point to the hashmap of children
            node = node.children[letter]
        # reached the end, mark it as one of the ends
        node.is_end = True
    
    def search(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        # return true if target is found whole if not false
        return node.is_end
    
    def delete(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                print("word does not exist")
                return
            node = node.children[letter]
        
        node.is_end = False
        print(f"{word} deleted")



t = Trie()
t.insert("Math")
t.insert("Maths")
t.insert("Man")
t.insert("Mantel")

print(t.search("Maths")) # true
print(t.search("Man")) # true
print(t.search("Mane")) # false
print(t.search("Mantel")) # True
print(t.search("Mant")) # False

# t.delete("Man")
# print(t.search("Man")) # False
t.delete("Mantel")
print(t.search("Mantel")) # False
print(t.search("Man")) # true





    