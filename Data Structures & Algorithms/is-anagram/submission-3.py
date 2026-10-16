class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict1={}
        my_dict2={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            
            my_dict1[s[i]]=my_dict1.get(s[i],0)+1
            my_dict2[t[i]]=my_dict2.get(t[i],0)+1

        
        if my_dict1==my_dict2:
            return True
        return False
        