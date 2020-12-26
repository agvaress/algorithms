# Find min or max number in array of number using recursion


def max_number(A, length):
    if length == 1:
        return A[0]
    return max(A[length - 1], max_number(A, length - 1))

A = [2, 4, 45, 6, -50, 10, 2]
l = len(A)

print(max_number(A, l))


