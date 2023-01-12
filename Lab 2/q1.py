class Stack:
    def __init__(self):
        self.top = -1
        # this stack is implemented with Python list (array)
        self.data = []

    def push(self, value):
        # increment the size of data using append()
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value
        pass

    def pop(self):
        value = self.data[self.top]
        # delete the top value using del
        del self.data[self.top]
        self.top -= 1
        return value

    def isEmpty(self):
        return (self.top == -1)

    def peek(self):
        pass

    def printStack(self):
        print(self.data)

    def invert(self):
        # remove pass and add your code here

        tmpStack = Stack()
        while not self.isEmpty():
            tmpStack.push(self.pop())
        self.data = tmpStack.data
        self.top = tmpStack.top


array = input("Enter a list of numbers separated by commas:\n")
array = [int(x) for x in array.split(",")]

s = Stack()
for n in array:
    s.push(n)

s.printStack()
s.invert()
s.printStack()
s.invert()
s.printStack()