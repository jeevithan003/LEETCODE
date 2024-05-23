class Solution:
    def isValid(self, s: str) -> bool:
        if "()" in s:
            s=s.replace("()","")
        if "{}" in s:
            s=s.replace("{}","")
        if "[]"in s:
            s=s.replace("[]","")
        
        if len(s)==0:
            return True
        else:
            return False
        
        
        
