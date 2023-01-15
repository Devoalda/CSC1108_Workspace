class Stack:
    # Complete the code here
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, value):
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        value = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        return value

    def peek(self):
        if len(self.data) != 0 or self.top != -1:
            return self.data[self.top]
        else:
            return "Stack is empty"
    def printStack(self):
        print(self.data)



def main():
    tmpStack = Stack()

    print(tmpStack.peek())

    tmpStack.push(10)
    topOfStack = tmpStack.peek()
    assert (topOfStack == 10), f"Top of stack not 10, got:{topOfStack}"

    tmpStack.push(11)
    topOfStack = tmpStack.peek()
    assert (topOfStack == 11), f"Top of stack not 11, got:{topOfStack}"

    tmpStack.push(12)
    topOfStack = tmpStack.peek()
    assert (topOfStack == 12), f"Top of stack not 12, got:{topOfStack}"

    tmpStack.push(13)
    topOfStack = tmpStack.peek()
    assert (topOfStack == 13), f"Top of stack not 13, got:{topOfStack}"

    tmpStack.push(14)
    topOfStack = tmpStack.peek()
    assert (topOfStack == 14), f"Top of stack not 14, got:{topOfStack}"

    tmpStack.pop()
    topOfStack = tmpStack.peek()
    assert (topOfStack == 13), f"Top of stack not 13, got:{topOfStack}"

    tmpStack.pop()
    topOfStack = tmpStack.peek()
    assert (topOfStack == 12), f"Top of stack not 12, got:{topOfStack}"

    print("No Errors! Stack contents: ")
    tmpStack.printStack()


if __name__ == "__main__":
    main()
