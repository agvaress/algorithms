# 1. Recursion
# O(2^n) time (each fib calls 2 another fibs) | O(n) space
def fibonacci_recursion(num):
    '''Return a fibonacci sequence value of num'''
    if num == 2:
        return 1
    elif num == 1:
        return 0
    else:
        return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2)


print(fibonacci_recursion(20))

# 2. Recursion + dict to store repeated values
# O(n) time | O(n) space
def getNthFib(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return n
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]

# 3. O(n) time | O(1) space
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

# 4. Find sum of n member of Fibonacci Sequence
fib1 = fib2 = 1
n = input("Enter number: ")
n = int(n)

i = 0

while i < n - 2:
    fib_sum = fib1 + fib2
    fib1, fib2 = fib2, fib_sum
    i += 1

print(fib_sum)

# 2. Generate Fibonacci Sequence
def generate_fib(n):
    fib_seq = []
    fib1 = fib2 = 1
    fib_seq.append(fib1)
    fib_seq.append(fib2)

    for el in range(2, n):
        fib_sum = fib1 + fib2
        fib1, fib2 = fib2, fib_sum
        fib_seq.append(fib2)

print(generate_fib(7))

# 4. Sum of even numbers
#Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
#Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

x = 0	#найти сумму чётных чисел
k = 4000000	#до 4м
fib1 = fib2 = 1
while 1 > 0:
    fib1, fib2 = fib2, fib1+fib2
    print(fib2)	#показывает ряд, начиная с 2
    if fib2 >= k:
        break
    elif fib2 % 2 == 0:
        x += fib2
print("сумма чётных = " + str(x))