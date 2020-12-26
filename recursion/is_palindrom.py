# O(n) - time, O(n) - space
def is_palidrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palidrome(s[1:-1])
