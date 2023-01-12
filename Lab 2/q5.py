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

    def pop(self):
        value = self.data[self.top]
        # delete the top value using del
        del self.data[self.top]
        self.top -= 1
        return value

    def isEmpty(self):
        return (self.top == -1)

    def printStack(self):
        print(self.data)


def checkBrace(s):
    stack = Stack()
    for i in s:
        if i == "(" or i== "[" or i == "{":
            stack.push(i)
        elif i == ")" or i == "]" or i == "}":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False

array = input("Enter a string to check:\n")

if checkBrace(array):
    print("The string", array, "is balanced")
else:
    print("The string", array, "is not balanced")