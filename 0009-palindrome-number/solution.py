class Solution(object):
    def isPalindrome(self, x):
        temp = x
        rev = 0

        if x < 0:
            return False

        while x != 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10

        return temp == rev
