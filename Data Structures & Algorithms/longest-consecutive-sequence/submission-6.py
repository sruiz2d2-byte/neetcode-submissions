class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict={}
        nums_s=set(nums)
        size=len(nums_s)
        nums_sb=set()
        c=0
        i=0
        if len(nums_s)==0:
            return 0 
        while c<len(nums_s):
            min_num=min(nums_s)

            while min_num+1 in nums_s:
                nums_sb.add(min_num)
                my_dict[i]=my_dict.get(i,0)+1
                min_num+=1

            
            nums_sb.add(min_num)
            my_dict[i]=my_dict.get(i,0)+1
            
            nums_s-=nums_sb
            
            i+=1

        res=max(my_dict.values())
                
        return res


