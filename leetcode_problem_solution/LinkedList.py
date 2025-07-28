class Nodes:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Nodes(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.nextNode = new_node
        self.tail = new_node

    def printNodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=' -> ')
            current_node = current_node.nextNode
        print("None")

linkedList = LinkedList()
linkedList.printNodes()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
linkedList.push(4)
linkedList.printNodes()