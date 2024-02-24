class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s1 = list(s)
        rev = list((reversed(s1)))
        if s1 == rev:
            return True
        else:
            return False
        