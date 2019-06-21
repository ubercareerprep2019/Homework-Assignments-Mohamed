from Part4 import LinkedList
def main():
    testPushBackAddsOneNode()
    testPopBackRemovesCorrectNode()
    testEraseRemovesCorrectNode()
    testEraseDoesNothingIfNoNode()
    testElementAtReturnNode()
    testElementAtReturnsNoNode()
    testSizeReturnsCorrectSize()

def testPushBackAddsOneNode():
    ll = LinkedList()
    ll.pushBack(1)
    assert(ll.length == 1)
    assert(ll.tail.value == 1 and ll.head.value == 1)

def testPopBackRemovesCorrectNode():
    ll = LinkedList()
    ll.pushBack(1)
    ll.pushBack(5)
    ll.pushBack(7)
    assert(ll.popBack() == 7)

def testEraseRemovesCorrectNode():
    ll = LinkedList()
    ll.pushBack(4)
    ll.pushBack(2)
    assert(ll.erase(1) == 2)

def testEraseDoesNothingIfNoNode():
    ll = LinkedList()
    assert(ll.erase(13) is None)

def testElementAtReturnNode():
    ll = LinkedList()
    ll.pushBack(1)
    ll.pushBack(5)
    ll.pushBack(7)
    assert(ll.elementAt(1) == 5)

def testElementAtReturnsNoNode():
    ll = LinkedList()
    ll.pushBack(1)
    ll.pushBack(5)
    ll.pushBack(7)
    assert(ll.elementAt(454) is None)

def testSizeReturnsCorrectSize():
    ll = LinkedList()
    assert(ll.size() == 0)
    ll.pushBack(1)
    assert (ll.size() == 1)
    ll.pushBack(5)
    assert (ll.size() == 2)
    ll.pushBack(7)
    assert (ll.size() == 3)
    ll.erase(0)
    assert (ll.size() == 2)



if __name__ == '__main__':
    main()