class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        b={"{":"}","[":"]","(":")"}
        
        for c in s:
            if c in b.keys():
                stack.append(c)
            elif c in b.values():
                if not stack:
                    return False
                elif b[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True