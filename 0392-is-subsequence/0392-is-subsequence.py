class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t=iter(t)
        return all(char in t for char in s)
                
                
        