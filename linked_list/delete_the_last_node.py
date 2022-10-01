class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertANewNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    print("the node is none")
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def delLastNode(self):
        lastNode = self.head

        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
            

        previousNode.next = None
