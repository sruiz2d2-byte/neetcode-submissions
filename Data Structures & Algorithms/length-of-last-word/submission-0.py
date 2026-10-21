class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        f=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                c=i
                break
        for i in range(c,-1,-1):
            if s[i]==" ":
                break
            f+=1
            

        return f