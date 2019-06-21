class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.min = None

    def setnext(self, nextnode):
            self.nextnode = nextnode

    def getvalue(self):
        return self.value


class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def pushBack(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.setnext(node)
            self.tail = node
        self.length = self.length + 1

    def popBack(self):
        removedData = None
        if self.isEmpty():
            return None
        elif self.length == 1:
            removedData = self.head.value
            self.head = None
            self.tail = None
        else:
            curr = self.head
            previous = self.head
            while curr.nextnode:
                previous = curr
                curr = curr.nextnode
            removedData = self.tail.value
            previous.setnext(None)
            self.tail = previous
        self.length = self.length - 1
        return removedData

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return
        node = Node(data)
        if self.isEmpty():
            self.pushBack(data)
        elif index == 0:
            node.setnext(self.head)
            self.head = node
        elif index == self.length - 1:
            self.pushBack(data)
        else:
            curr = self.head
            previous = self.head
            i = 0
            while i < index:
                previous = curr
                curr = curr.nextnode
                i+=1
            node.setnext(curr)
            previous.setnext(node)
        self.length = self.length + 1

    def erase(self, index):
        removedData = None
        if index < 0 or index > self.length:
            return
        if self.isEmpty():
            return
        elif self.length == 1:
            return self.popBack()
        elif index == 0:
            removedData = self.head.value
            self.head = self.head.nextnode
        else:
            curr = self.head
            previous = self.head
            i = 0
            while i < index:
                previous = curr
                curr = curr.nextnode
                i+=1
            removedData = curr.value
            previous.setnext(previous.nextnode.nextnode)
        self.length = self.length - 1
        return removedData

    def elementAt(self, index):
        if index < 0 or index > self.length:
            return

        if self.isEmpty(): return None
        elif self.length == 1: return self.head.value
        elif index == 0: return self.head.value
        elif index == self.length - 1: return self.tail.value
        else:
            curr = self.head
            i = 0
            while i < index:
                curr = curr.nextnode
                i+=1
            return curr.value

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def printList(self):
        curr = self.head
        while curr:
            print str(curr.value) + "\n"
            curr = curr.nextnode

    def hasCycle(self):
        visited = set()
        curr = self.head
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
        return False

    def isAPalindrome(self):
        fast = self.head
        slow = self.head
        while fast and fast.nextnode:
            fast = fast.nextnode.nextnode
            slow = slow.nextnode
        node = None
        self.flip(slow)
        while node:
            if node.value != self.head.value:
                return False
            node = node.nextnode
            head = head.nextnode
        return True

    def flip(self, slow):
        node = None
        while slow:
            next = slow.nextnode
            slow.nextnode = node
            node = slow
            slow = next

