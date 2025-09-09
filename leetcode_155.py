#Design a stack with each function O(1)
#push,pop,top/peek,getMin

class MinStack():
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self,value):
        self.stack.append(value)
        if self.mins==[] or value < self.mins[-1]:
            self.mins.append(value)
    def pop(self):
        self.stack.pop()
        self.mins.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mins[-1]
    def display(self):
        print(self.stack)
    
minStack = MinStack()
minStack.push(-2)
minStack.display()
minStack.push(0)
minStack.display()
minStack.push(-3)
minStack.display()
m = minStack.getMin()
print(m)
minStack.pop()
minStack.display()
t = minStack.top()
print(t)
z = minStack.getMin()
print(z)
