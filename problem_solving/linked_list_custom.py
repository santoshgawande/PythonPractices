#LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFirst(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printllist(self):
        temp = self.head
        if temp == None:
            print('linkedlist is empty')
        elif temp.next == None :
            print(temp.data)
        else :
            printllist(temp.next)


llist = LinkedList()
llist.insertAtFirst(5)
llist.printllist()
