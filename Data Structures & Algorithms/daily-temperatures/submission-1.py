class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        mstack:list[tuple]=[]
        
        
        i=len(temperatures)-1
        while i>=0:
            
            if mstack:
                if mstack[-1][0]>temperatures[i]:
                    res[i]=mstack[-1][1]-i
                    mstack.append((temperatures[i],i))
                   
                    
                else:
                    mstack.pop()
                    
                    continue
            else:
                mstack.append((temperatures[i],i))
                
              
                
                
            
            i-=1
        
        return res
            
            