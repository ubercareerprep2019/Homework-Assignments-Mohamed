import copy
import random
from arraysAndStrings import isStringPermutation, pairsThatEqualSumArray
# returns random string of length size
def randomInput(size):
    list = ['-1'] * size
    for i in range(len(list)):
        list[i] = chr(random.randint(97, 122))
    return list

# returns permuted string s
def permute(s):
    permuted = copy.deepcopy(s)
    taken = set()
    for i in range(len(permuted)):
        randomIndex = random.randint(0, len(s) - 1)
        if randomIndex in taken:
            while randomIndex in taken:
                randomIndex = (randomIndex + 1) % len(s)
            permuted[i] = s[randomIndex]
        else:
            permuted[i] = s[randomIndex]
        taken.add(randomIndex)
    return permuted

def testIsStringPermutation():
    isStringPermutation("", "daw")  # strings of different size
    isStringPermutation([1, 2, 3], "daw")  # input is not string
    # test random permuted strings
    numberOfTests = 1000
    for i in range(numberOfTests):
        randomSize = random.randint(1, 1000)
        input1 = randomInput(randomSize)
        input2 = permute(input1)
        s1 = ''.join(input1)
        s2 = ''.join(input2)
        assert len(s1) == len(s2)
        if not isStringPermutation(s1, s2):
            print "UNEXPECTED OUTPUT:\ns1:%s   s2:%s" % (s1, s2)
    # test random strings that aren't permutations of each other
    for i in range(numberOfTests):
        randomSize = random.randint(1, 1000)
        input1 = randomInput(randomSize)
        input2 = randomInput(randomSize)
        s1 = ''.join(input1)
        s2 = ''.join(input2)
        assert len(s1) == len(s2)
        if isStringPermutation(s1, s2):
            print "UNEXPECTED OUTPUT:\ns1:%s   s2:%s" % (s1, s2)

def testPairsThatEqualSumArray():
    print pairsThatEqualSumArray([1, 3, 5, -5, 9, 4, 3, 2, 11, 1, 3, 5, -5, 9, 4, 3, 2, 11], 6)
    print pairsThatEqualSumArray([], 1)


def main():
    testIsStringPermutation()
    # testPairsThatEqualSumArray()


if __name__ == '__main__':
    main()