# O(long(n)) - time
# O(nlog(n)) - space

# 1. Educational example
def merge_sorted_arrays(A: list, B: list):
    C = [0] * (len(A) + len(B))
    #A[i]
    #B[k]
    #C[n]
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    # append rest of elements of A to C
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    # append rest of elements of B to C
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):
    if len(A) <= 1:
        return
     middleIdx = len(A) // 2
    L = A[:middleIdx]
    R = A[middleIdx:len(A)]
    merge_sort(L)
    merge_sort(R)
    C = merge_sorted_arrays(L, R)
    # from merged C copy to A
    A[:] = C[:]
    return A

print(merge_sort([5,2,8,1,0,7,2]))


# 2. Python style example
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf,rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray
