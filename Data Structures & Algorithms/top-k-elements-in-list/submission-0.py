class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}

        for num in nums:
            my_dict[num]=my_dict.get(num,0)+1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key,freq in my_dict.items():

            buckets[freq].append(key)

        res=[]

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res