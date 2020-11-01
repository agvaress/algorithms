# Sum numbers like:
# 0 1 2 3 4 5 ...

def sum(num):
    if num == 1:
        return 1  # exit function with value 1
    else:
        return num + sum(num-1)


print(sum(5))
