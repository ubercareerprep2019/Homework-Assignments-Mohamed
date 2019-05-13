# This function takes two strings and returns true if one string is a permutation of
# the other, false otherwise.
def isStringPermutation(s1, s2):
    if not isinstance(s1, basestring) and isinstance(s2, basestring):
        print('Argument must be string type!')
        return False

    if len(s1) != len(s2):
        return False # two strings can't be perumtations if they are not of the same length

    characters = [0] * 256 # hold every occurence of every possible ascii character (256 total and default 0 occurences)

    # count all occurences of charactes in s1
    for char in s1:
        characters[ord(char)] += 1

    # decrement all occurrences of characters in s2 from s1
    for char in s2:
        characters[ord(char)] += -1

    # check if all occurences have returned to 0, if not return false
    for char in characters:
        if char != 0: return False

    # otherwise, return true
    return True

# This function takes an array of integers and a target integer to which the array
# elements must sum. It returns an array of all pairs of integers from the input
# array whose sum equals the target.
def pairsThatEqualSumArray(arr, target):
    if len(arr) == 0:
        return []
    print arr
    print ""
    dictionary = dict()
    pairs = []
    # for e, i in enumerate(arr):
    #     dictionary[i] = e

    # for i in range(len(arr)):

    banished = set()
    for i in range(len(arr)):
        if (target - arr[i]) in dictionary and dictionary[target - arr[i]] != i:
            if dictionary[target - arr[i]] < i:
                if arr[i] not in banished and target-arr[i] not in banished:
                    pairs.append((arr[i], target - arr[i]))
                    banished.add(arr[i])
                    banished.add(target - arr[i])
                    dictionary[arr[i]] = i

                if arr[i] in dictionary: dictionary.pop(arr[i])
                if arr[i] != target - arr[i]:
                    if target - arr[i] in dictionary: dictionary.pop(target - arr[i])
        else:
            dictionary[arr[i]] = i

    return pairs