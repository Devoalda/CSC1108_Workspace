class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def insert(self, node):
        if self.head is None:
            self.head = self.prev = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def delete(self, value):
        temp = self.head
        while temp is not None and temp.data is not value:
            temp = temp.next
        if temp is None:
            print("Error, value not found")
        else:
            if temp is self.head:
                self.head = self.head.next
            elif temp is self.tail:
                self.tail = self.tail.prev
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

    def peek(self):
        return self.head.data

    def search(self, value):
        temp = self.head
        counter = 0
        while temp is not None and temp.data is not value:
            temp = temp.next
            counter += 1
        if temp is None:
            print("Error: Unable to search")
        else:
            return counter

    def printList(self):
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print(temp.data, end=" -> ")
            else:
                print(temp.data)
            temp = temp.next


def main():
    dll = doublyLinkedList()
    dll.insert(node(5))
    dll.insert(node(6))
    dll.insert(node(7))

    dll.printList()
    # Asserts
    assert(dll.peek() == 7), f"Top of Doubly Linked List not 7, got:{dll.peek()}"
    assert(dll.search(5) == 2), f"Index of 5 not 2, got:{dll.search(5)}"
    assert(dll.search(6) == 1), f"Index of 6 not 1, got:{dll.search(6)}"
    assert(dll.search(7) == 0), f"Index of 7 not 0, got:{dll.search(7)}"

    print("All tests passed")
    dll.printList()

if __name__ == "__main__":
    main()
