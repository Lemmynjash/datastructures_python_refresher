class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAsTheHead(self, newNode):
        tempo = self.head
        self.head = newNode
        self.head.next = tempo
        del tempo

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

    def printNode(self):
        if self.head is None:
            print("the node is none")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


node = Node("Lemmy")
linkedList = LinkedList()
linkedList.insertNewNode(node)
node2 = Node("Jackline")
linkedList.insertNewNode(node2)
node3 = Node("Mathew")
linkedList.insertNewNode(node3)
linkedList.printNode()
print("-------------------Inserting a node as the head----------")
node4 = Node("Kamau")
linkedList.insertNodeAsTheHead(node4)
linkedList.printNode()
