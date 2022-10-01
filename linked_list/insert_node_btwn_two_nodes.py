class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def insertNewNodeAtTheHead(self, newNode):
        tempo = self.head
        self.head = newNode
        self.head.next = tempo
        del tempo

    def printNode(self):
        if self.head is None:
            print("the node is none")
            return

        while True:
            if self.head is None:
                break

            print(self.head.data)

    def listLength(self):
        currentLength = 0
        while self.head is not None:
            currentLength += 1
            self.head = self.head.next

        return currentLength

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("invalid position")
            return
        if position is 0:
            self.insertNewNodeAtTheHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0

        while True:

            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            # advancing to the next node
            currentNode = currentNode.next
            # advance the current position
            currentPosition += 1
