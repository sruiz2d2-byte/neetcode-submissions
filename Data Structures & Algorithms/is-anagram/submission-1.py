class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        my_dict1={}
        dict2={}
        for i,s1 in enumerate(s):
            my_dict1[s1]=my_dict1.get(s1,0)+1
            dict2[t[i]]=dict2.get(t[i],0)+1
        
        if my_dict1==dict2:
            return True
        return False


