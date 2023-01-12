class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # return the value of the node at index

    def search(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('search error: invalid index')
        else:
            return temp

    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, value):
        prev = None
        temp = self.head

        while temp != None and temp.data != value:
            prev = temp
            temp = temp.next

        # node to be deleted is head
        if temp == self.head:
            self.deleteAtHead()

        # Value found
        elif temp != None:
            prev.next = temp.next
            del temp
        # Value not found
        else:
            print('Value ', value, ' cannot be found')

    # delete the node at index
    def deleteAt(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('search error: invalid index')
        else:
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
            del temp

    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def printList(self):
        output = "Current list content: [ "
        temp = self.head
        while temp is not None:
            output += str(temp.data) + " "
            temp = temp.next
        output += "]"
        print(output)

    # return the number of elements in the queue
    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size


class Queue:
    def __init__(self):
        # You must implement this Queue with a SinglyLinkedList
        self.q = SinglyLinkedList()

    def enqueue(self, value):
        # remove pass and add your code here
        self.q.insertAtHead(SinglyListNode(value))

    def printQueue(self):
        self.q.printList()

    def dequeue(self):
        self.q.deleteAt(self.q.size() - 1)

    def isEmpty(self):
        return self.q.size() == 0

    def peek(self):
        return self.q.search(self.q.size() - 1).data


Q = Queue()

array = input("Enter a list of command separated by commas:\n")
array = [x for x in array.split(",")]

for cmd in array:
    if cmd.startswith("I"):
        print("Checking if queue is empty")
        print(Q.isEmpty())
    elif cmd.startswith("E"):
        c, v = cmd.split()
        Q.enqueue(int(v))
        print("After enqueuing", int(v))
        Q.printQueue()
    elif cmd.startswith("P"):
        print("Peeking at queue")
        print(Q.peek())
    elif cmd.startswith("D"):
        Q.dequeue()
        print("After dequeing")
        Q.printQueue()
    else:
        print("Command not recognized!")