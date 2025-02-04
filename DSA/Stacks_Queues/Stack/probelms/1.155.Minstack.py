# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
    
    
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(3)
print(obj.min_stack)
print(obj.getMin())
obj.pop()
print(obj.getMin())

# revisited the question, different answer
class MinStack:

    def __init__(self):
        self.stk=[]
        self.min= []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.stk.pop():
            self.min.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]