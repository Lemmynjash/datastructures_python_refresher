# create node
# create linked list
# add nodes to linked list
# print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNewNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            # Head--->Lemmy--->Jackline---None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def printList(self):
        # head--->Lemmy--->Jackline--->Mathew
        currentNode = self.head
        if currentNode is None:
            print("The list is empty")
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node --> data,next
# first node will look like this
# DATA--> Lemmy NEXT--->None
firstNode = Node("Lemmy")
# by linking the first node with the second node this is where linked list comes in
linkedList = LinkedList()
# head--->Lemmy--->None
linkedList.insertNewNode(firstNode)
# head--->Lemmy--->Jackline--->None
secondNode = Node("Jackline")
linkedList.insertNewNode(secondNode)
thirdNode = Node("Mathew")
# head--->Lemmy--->Jackline--->Mathew---->None
linkedList.insertNewNode(thirdNode)
# lets print this
linkedList.printList()
