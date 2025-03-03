# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        if root == None:
            return "n"

        ser_str = ""
        ser_str +=str(root.val)
        ser_str += "," + self.serialize(root.left) 
        ser_str += "," + self.serialize(root.right)

        return ser_str
        

    def deserialize(self, data):
        def deserialize_helper(ser_data):
            val = ser_data.pop()
            if val == "n":
                return None

            root = TreeNode(int(val)) # create tree fron NODE -> LEFT -> RIGHT
            root.left = deserialize_helper(ser_data)
            root.right = deserialize_helper(ser_data)

            return root

        ser_data = []
        pi = len(data)
        
        # append the data from the end, so i can eaisly pop the list to get the first element
        for i in range(len(data)-1, -1, -1):
            if data[i] != ",":
                continue
            ser_data.append(data[i+1:pi])
            pi =i


        ser_data.append(data[i:pi])

        return deserialize_helper(ser_data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))