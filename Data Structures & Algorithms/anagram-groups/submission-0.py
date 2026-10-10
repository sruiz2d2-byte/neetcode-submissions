class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1:dict[tuple:list[str]]={}
        
        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index]+=1
            
            key=tuple(count)
            if key in dict1:
                dict1[key].append(word)
            else:
                dict1[key]=[]
                dict1[key].append(word)
        l:list=[]
        for k,v in dict1.items():
            l.append(v)
        return l 