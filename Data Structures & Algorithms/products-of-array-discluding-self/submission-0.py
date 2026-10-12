class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]
        sufx=[1]
        for i in range(0,len(nums)-1):
            pref.append(pref[i]*nums[i])
            
        for i in range(len(nums)-1,0,-1):
            sufx.append(sufx[-1]*nums[i])

        sufx.reverse()

        res=[]
        for i in range(len(nums)):
            res.append(pref[i]*sufx[i])
        return res
