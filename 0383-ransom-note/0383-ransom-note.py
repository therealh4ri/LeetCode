class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = {}
        magazine_count = {}
        
        for c in ransomNote:
            if c in ransom_count:
                ransom_count[c]+=1
            else: 
                 ransom_count[c]=1
        
         
        for c in magazine:
            if c in magazine_count:
                magazine_count[c]+=1
            else: 
                 magazine_count[c]=1
                    
        for c,count in ransom_count.items():
            if c not in magazine_count or magazine_count[c] < count :
                return False
            
            
        return True
        
        