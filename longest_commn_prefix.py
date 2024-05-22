class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0][:2:]
        length=len(strs)
        last=strs[length-1][:2:]
        if first==last:
            return first
        return ""
