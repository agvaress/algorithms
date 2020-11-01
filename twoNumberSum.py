# Two number sum
# Find target sum among 2 numbers in an array.

a = [3, 5, -4, 8, 11, 1, -1, 6]

# 1. Two loops.
# O(2^n) time | O(n) space

def twoNumberSum(array, targetSum):
    for i in range(0, len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


print(twoNumberSum(a, 10))

# 2. hash table
# Using the formula below check if values presents in a hash table
# x + y = 10
# targetSum = 10, currentNum = x
# y = 10 - x
# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        match = targetSum - num # <-- this is "y"
        if match in nums:
            return [match, num]
        else:
            nums[num] = True
    return []
