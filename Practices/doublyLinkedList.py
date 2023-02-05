class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1


    def delete(self, value):
        temp = self.head
        while temp is not None and temp.data is not value:
            temp = temp.next
        if temp is None:
            print("Error: value not found")
        elif temp is self.head:
            self.head = self.head.next
        elif temp is self.tail:
            self.tail = self.tail.prev
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp

    def peek(self):
        return self.head.data

    def search(self, value):
        temp = self.head
        counter = 0
        while temp is not None and temp.data is not value:
            temp = temp.next
            counter += 1
        if temp is None:
            print("Error: value not found")
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
    assert(dll.peek() == 5), f"Top of queue not 5, got:{dll.peek()}"
    assert(dll.search(6) == 1), f"6 not found at index 1, got:{dll.search(6)}"
    dll.delete(6)
    assert(dll.search(7) == 1), f"7 not found at index 1, got:{dll.search(7)}"

    dll.insert(node(8))
    dll.insert(node(9))
    assert(dll.search(9) == 3), f"9 not found at index 3, got:{dll.search(9)}"
    dll.delete(9)

    print("All tests passed")
    dll.printList()

if __name__ == "__main__":
    main()
