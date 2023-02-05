class queue:
    def __init__(self):
        self.data = []
        self.rear = -1

    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        value = self.data[0]  # Dequeue from the front
        del self.data[0]
        self.rear -= 1
        return value

    def peek(self):
        if self.rear != -1 and self.data is not None:
            return self.data[self.rear]
        else:
            return "Empty Queue"

    def printQueue(self):
        return(self.data)

def main():
    q1 = queue()

    print(q1.printQueue())
    q1.enqueue(10)
    assert(q1.peek() == 10), f"Top of queue not 10, got:{q1.peek()}"
    q1.enqueue(11)
    assert(q1.peek() == 11), f"Top of queue not 11, got:{q1.peek()}"

    print(q1.printQueue())

    q1.dequeue()
    assert(q1.peek() == 11), f"Top of queue not 11, got:{q1.peek()}"
    print(q1.printQueue())
    q1.dequeue()
    assert(q1.peek() == "Empty Queue"), f"Top of queue not Empty Queue, got:{q1.peek()}"

    print("No errors found")
    print(q1.printQueue())

if __name__ == "__main__":
    main()
