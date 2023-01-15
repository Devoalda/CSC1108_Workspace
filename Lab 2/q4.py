# Enter your code here. Read input from STDIN. Print output to STDOUT
class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.data = []

    def search(self, value):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < value:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('Error: invalid index')
        else:
            return temp
    def insert(self, node, index):
        if index == 0:
            self.insertAtHead(node)
        else:
            temp = self.search(index)
            if temp is not None:
                node.next = temp.next
                temp.next = node
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
        output = "[ "
        temp = self.head
        while temp is not None:
            output += str(temp.data) + " "
            temp = temp.next
        output += " ]"
        print(output)

    # return the number of elements in the queue
    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size


def mergeList(list1, list2):
    mergedList = SinglyLinkedList()

    # Merge and sort list
    for i in range(list1.size()):
        if mergedList.search(list1.search(i).data) is None:
            mergedList.insert(SinglyListNode(list1.search(i).data), mergedList.size())
        elif list1.search(i).data < mergedList.search(list1.search(i).data).data:
            mergedList.insert(SinglyListNode(list1.search(i).data), mergedList.size())



    print("Content of merged list")
    mergedList.printList()


def reverse(array):
    reversed_array = []
    for i in range(len(array)):
        reversed_array.append(array[len(array) - 1 - i])
    return reversed_array


array1 = input("Enter a list of numbers in descending order for list 1 seperated by commas:")
array1 = [x for x in array1.split(",")]
array1 = reverse(array1)
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()

for n in array1:
    list1.insertAtHead(SinglyListNode(n))

array2 = input("\nEnter a list of numbers in descending order for list 2 seperated by commas:")
array2 = [x for x in array2.split(",")]
array2 = reverse(array2)

for n in array2:
    list2.insertAtHead(SinglyListNode(n))

print("Content of list1")
list1.printList()

print("Content of list 2")
list2.printList()
mergeList(list1, list2)