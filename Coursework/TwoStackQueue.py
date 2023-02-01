#!/bin/python3

class Stack:
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

    def isEmpty(self):
        return self.top == -1


def enqueue(stack1, value):
    stack1.push(value)


def dequeue(stack1, stack2):
    if stack2.isEmpty():
        while not stack1.isEmpty():
            stack2.push(stack1.pop())
    return stack2.pop()


def peek(stack1, stack2):
    if stack2.isEmpty():
        while not stack1.isEmpty():
            stack2.push(stack1.pop())
    return stack2.data[stack2.top]


if __name__ == '__main__':
    stack1 = Stack()
    stack2 = Stack()

    # Get number of queries
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().rstrip().split())))
        query = queries[i][0]
        # if the query is 1, enqueue
        if query == 1:
            enqueue(stack1, queries[i][1])
        # if the query is 2, dequeue
        elif query == 2:
            dequeue(stack1, stack2)
        # if the query is 3, print the top of the queue
        elif query == 3:
            print(peek(stack1, stack2))
