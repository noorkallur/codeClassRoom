# creating a trie using a hashmap

# TRIE Node structure
class Node:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Flag to indicate end of a word

# TRIE class
class Trie:
    def __init__(self):
        self.root = Node()  # Root node of the Trie

    def insert(self, word):
        node = self.root
        for letter in word:
            # If the letter is not present, add a new node
            if letter not in node.children:
                node.children[letter] = Node()
            # Move to the child node
            node = node.children[letter]
        # Mark the end of the word
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for letter in word:
            # If the letter is not present, word doesn't exist
            if letter not in node.children:
                return False
            node = node.children[letter]
        # Return True if the word exists and is marked as end
        return node.is_end
    
    def delete(self, word):
        # Helper function for recursive deletion
        def delete_helper(node, i):
            # If reached the end of the word
            if i == len(word):
                if not node.is_end:
                    return False  # Word not found
                
                node.is_end = False  # Unmark the end of word
                print(f"{word} deleted")
                # If node has no children, it can be deleted
                return len(node.children) == 0
                
            if word[i] not in node.children:
                return False  # Word not found
            
            print(word[i])
            # Recursively delete the child node
            child_delete = delete_helper(node.children[word[i]], i+1)
            if child_delete:
                print(f"deleting {word[i]}")
                # Remove the child node if it can be deleted
                node.children.pop(word[i])
                # Return True if current node has no children and is not end of another word
                return len(node.children) == 0 and not node.is_end
            return False

        # Start deletion from the root node
        return delete_helper(self.root, 0)

# Example usage
t = Trie()
t.insert("Math")
t.insert("Maths")
t.insert("Man")
t.insert("Mantel")
t.insert("Manter")

# Uncomment to test search functionality
# print(t.search("Maths")) # true
# print(t.search("Man")) # true
# print(t.search("Mane")) # false
# print(t.search("Mantel")) # True
# print(t.search("Mant")) # False

# Uncomment to test delete functionality
# t.delete("Man")
# print(t.search("Man")) # False
print(t.delete("Mantel"))  # Delete "Mantel"
print(t.search("Mantel"))  # Should be False after deletion
print(t.search("Manter"))  # Should be True
# t.delete("Man")
# print(t.search("Mantel")) # False
# print(t.search("Man")) # true