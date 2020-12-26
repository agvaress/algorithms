# Selection sort
# Slow sort algorithm.
# O(n^2) time | O(1) space


a = [5, 3, 6, 2, 10, 4]


def selectionSort(array):
    currentIndx = 0
    while currentIndx < len(array) - 1:
        smallestIndx = currentIndx
        # Interact through unsorted sublist
        for i in range(currentIndx + 1, len(array)):
            if array[smallestIndx] > array[i]:
                smallestIndx = i
        swap(currentIndx, smallestIndx, array)
        currentIndx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(selectionSort(a))
