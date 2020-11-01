a = [3, 5, -4, 8, 11, 1, -1, 6]

b = [3, 8, 6]

# Is b subsequence of a (contains the same elements in hte same order)
# O(n) - time | O(1) - space

def validateSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)


# O(n) - time | O(1) - space
def validateSubsequence(array, sequence):
    sequenceIdx = 0
    for el in array:
        if sequenceIdx == len(sequence):
            break
        if el == sequence[sequenceIdx]:
            sequenceIdx += 1
        return sequenceIdx == len(sequence)