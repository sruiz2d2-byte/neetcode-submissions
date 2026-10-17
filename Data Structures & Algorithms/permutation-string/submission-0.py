class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        size1=len(s1)
        count2={}
        count1={}
        for i in range(len(s1)):
            count2[s1[i]]=count2.get(s1[i],0)+1
            count1[s2[i]]=count1.get(s2[i],0)+1

        l=0
        if count1 == count2:
            return True

        for r in range(size1,len(s2)):
            
            count1[s2[l]]=count1.get(s2[l],0)-1
            count1[s2[r]]=count1.get(s2[r],0)+1
            if count1[s2[l]] == 0:
                del count1[s2[l]]
            l+=1

            if count1==count2:
                return True

        return False

            

            
         
