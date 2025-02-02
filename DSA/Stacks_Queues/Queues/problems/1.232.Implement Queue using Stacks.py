# noor solution
class MyQueue:

    def __init__(self):
        self.Q = []

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        if self.empty():
            return
        
        rev_stk = [] # reverse
        while len(self.Q):
            rev_stk.append(self.Q.pop())
        
        removed = rev_stk.pop() # pop last of the reverse
        
        while len(rev_stk):
            self.Q.append(rev_stk.pop()) # re-append to the Q
        
        return removed
        

    def peek(self) -> int:
        rev_stk = []
        while len(self.Q):
            rev_stk.append(self.Q.pop())
        
        peek = rev_stk[-1]
        
        while len(rev_stk):
            self.Q.append(rev_stk.pop())
        
        return peek
        

    def empty(self) -> bool:
        return len(self.Q) == 0

# Dev solution
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure output stack has the current front
        print(f"inp {self.input}")
        print(f"out {self.output}")
        return self.output.pop()

    def peek(self) -> int:
        if len(self.output) == 0:  # Transfer elements if output stack is empty
            while self.input:
                self.output.append(self.input.pop())
                
        print(f"inp {self.input}")
        print(f"out {self.output}")
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output

obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
obj.push(3)
print(obj.peek())
