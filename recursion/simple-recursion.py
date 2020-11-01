# Print out 'Hi there' 5 times using recursion


def privet(n):
    if n == 0:
        return
    else:
        print("Hi There!")
        privet(n-1)


print(privet(5))