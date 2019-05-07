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

