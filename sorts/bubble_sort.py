# O(n^2) - time
# O(1) - space

a = [5, 7, 4, 3, 8, 2]

# 1. Via 2x for
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for run in range(n - 1): # before last value to do not jump out of array[i + 1]
        for idx in range(n - 1 - run):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                count += 1
    print(f'substitutions: {count}')
    print()
    return arr


print(bubble_sort(a))

# 2. via while
def bubble_sort(arr):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1, arr)
                isSorted = False
        counter += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
