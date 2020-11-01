# 1. Using recursion

my_list = [11, 14, 22, 26, 46, 48, 67, 73, 77, 89]


def binary_search(l, num, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) / 2
        if num == l[mid]:
            return num
        elif num < l[mid]:
            return binary_search(l, num, start, mid - 1)
        elif num > l[mid]:
            return binary_search(l, num, mid + 1, stop)


start = 0
stop = len(my_list) - 1
num = 26

x = binary_search(my_list, num, start, stop)


if x is False:
    print('number {0} is not found'.format(num))
else:
    print('number {0} found'.format(num))


