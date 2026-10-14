class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        mstack:list[tuple]=[]
        
        
        i=len(temperatures)-1
        while i>=0:
            
            if mstack:
                if mstack[-1][0]>temperatures[i]:
                    res.append(mstack[-1][1]-i)
                    mstack.append((temperatures[i],i))
                   
                    
                else:
                    mstack.pop()
                    
                    continue
            else:
                mstack.append((temperatures[i],i))
                
                res.append(0)
                
                
            
            i-=1
        res.reverse()
        return res
            
            
