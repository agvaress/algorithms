def array_sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    return arr[0] + array_sum(arr[1:])


print(array_sum([3, 4, 5, 6]))


def len_array(arr):
    if len(arr) == 1:
        return 1
    return 1 + len_array(arr[1:])