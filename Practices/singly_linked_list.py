class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def search(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1
        if temp is None:
            print("Error: invalid index")
        else:
            return temp

    def searchValue(self, value):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None:
            if temp.data == value:
                return counter
            else:
                prev = temp
                temp = temp.next
                counter += 1

    def delete(self, value):
        temp = self.head
        prev = None
        while temp is not None and temp.data is not value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Error: value not found")
        elif temp.next == self.head:
            self.deleteAtHead()
        else:
            prev.next = temp.next
            del temp

    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head is None

    def printList(self):
        temp = self.head
        while temp is not None:
            print("[", temp.data, "]", end=" ")
            temp = temp.next


def main():
    linkL = SinglyLinkedList()

    # Nodes
    aNode = SinglyListNode(10)
    bNode = SinglyListNode(11)
    cNode = SinglyListNode(12)
    dNode = SinglyListNode(13)

    linkL.insertAtHead(aNode)
    linkL.insertAtHead(bNode)
    linkL.insertAtHead(cNode)
    linkL.insertAtHead(dNode)

    assert linkL.search(3).data == 10, f"Node containing 10 not found, got:{linkL.search(3).data}"
    assert linkL.search(2).data == 11, f"Node containing 11 not found, got:{linkL.search(2).data}"
    assert linkL.search(1).data == 12, f"Node containing 12 not found, got:{linkL.search(1).data}"
    assert linkL.search(0).data == 13, f"Node containing 13 not found, got:{linkL.search(0).data}"

    print("No Errors: Linked List Contents: ")
    linkL.printList()
    print()

    linkL.delete(12)
    print("After Deletion")
    assert linkL.search(1).data == 11, f"Node containing 11 not found, got:{linkL.search(1).data}"
    print("No Errors: Linked List Contents: ")
    linkL.printList()
    print()

    linkL.deleteAtHead()
    assert linkL.search(0).data == 11, f"Node containing 11 not found, got:{linkL.search(0).data}"
    print("No Errors: Linked List Contents: ")
    linkL.printList()
    print()

    assert linkL.searchValue(10) == 1, f"Index of node containing 10 not found, got:{linkL.searchValue(10)}"
    print("Index of node containing 10 is: ", linkL.searchValue(10))

    assert linkL.peek() == 11, f"Head of linked list is not 11, got:{linkL.peek()}"
    print("Head of linked list is: ", linkL.peek())

    linkL.deleteAtHead()
    linkL.deleteAtHead()

    assert linkL.isEmpty() == True, f"Linked list is not empty, got:{linkL.printList()}"
    print("Linked list is empty!")


if __name__ == "__main__":
    main()
