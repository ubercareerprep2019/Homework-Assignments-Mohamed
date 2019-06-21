from Part3 import Stack, Queue
import random

def main():
    testPushOntoEmptyStack()
    testPushOntoNonEmptyStack()
    testPopNonEmptyStack()
    testPopOneFromEmpty()
    testPopFromEmpty()
    testPushThenPop()
    testMin()

def emptyStack():
    return Stack()

def NonEmptyStack():
    stack = Stack()
    limit = random.randint(0, 50)
    for i in range(limit):
        stack.push(random.randint(0,10))
    return stack

def testPushOntoEmptyStack():
    stack = Stack()
    stack.push(1)
    assert(stack.peek() == stack.head)
    assert(stack.size == 1)

def testPushOntoNonEmptyStack():
    stack = NonEmptyStack()
    previous = stack.size
    node = stack.push(88)
    assert(stack.size == previous + 1)
    assert(stack.head == node)

def testPopNonEmptyStack():
    stack = NonEmptyStack()
    head = stack.peek().value
    previous = stack.size
    popped = stack.pop()
    assert(stack.size == previous - 1)
    assert(popped == head)

def testPopOneFromEmpty():
    stack = emptyStack()
    stack.push(1)
    stack.pop()
    assert(stack.size == 0)

def testPopFromEmpty():
    stack = emptyStack()
    popped = stack.pop()
    assert(popped == None)
    assert(stack.size == 0)

def testPushThenPop():
    stack = NonEmptyStack()
    previous = stack.size
    stack.push(2)
    stack.pop()
    stack.pop()
    assert(previous - 1 == stack.size)

def testMin():
    stack = emptyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert(stack.min() == 1)
    stack.push(-1)
    assert(stack.min() == -1)
    stack.pop()
    assert(stack.min() == 1)


if __name__ == '__main__':
    main()