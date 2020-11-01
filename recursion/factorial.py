# !5 = 5 * 4 * 3 * 2 * 1


def fact(num):
    if num == 1:
        return 1  # exit function with value 1, stop return
    else:
        return num * fact(num-1)


print(fact(5))

