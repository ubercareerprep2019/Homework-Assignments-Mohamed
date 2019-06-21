class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.min = None

    def setnext(self, nextnode):
            self.nextnode = nextnode

    def getvalue(self):
        return self.value


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, value):
        min = self.min()
        node = Node(value)
        temp = self.head
        self.head = node
        node.setnext(temp)
        self.size = self.size + 1
        if self.size == 1:
            node.min = value
        elif value < min:
            node.min = value
        else:
            node.min = min
        return node

    def pop(self):
        if self.isEmpty(): return None
        data = self.head.value
        self.head = self.head.nextnode
        self.size = self.size - 1
        return data

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        return self.head

    def printStack(self):
        print "-----------TOP------------\n"
        node = self.head
        while node:
            print str(node.value) + "\n"
            node = node.nextnode
        print "----------BOTTOM-----------\n"
        print "SIZE: " + str(self.size)

    def min(self):
        if self.isEmpty(): return None
        return self.head.min


class Queue:
    def __init__(self):
        self.stackToPush = Stack()
        self.stackToPop = Stack()
        self.size = 0

    def enqueue(self, value):
        self.stackToPush.push(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0: return None

        if self.stackToPop.isEmpty():
            self.transfer()

        data = self.stackToPop.pop()
        self.size = self.size - 1

        return data

    def transfer(self):
        while not self.stackToPush.isEmpty():
            popped = self.stackToPush.pop()
            self.stackToPop.push(popped)


    def printQueue(self):
        print "-----------TOP------------\n"
        node = self.stackToPop.head
        while node:
            print str(node.value) + "\n"
            node = node.nextnode
        self.printRest(self.stackToPush.peek())
        print "----------BOTTOM-----------\n"
        print "SIZE: " + str(self.size)

    def printRest(self, node):
        if node is None:
            return
        if node.nextnode is None:
            print str(node.value) + "\n"
            return
        self.printRest(node.nextnode)
        print str(node.value) + "\n"













