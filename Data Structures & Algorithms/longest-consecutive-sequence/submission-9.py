class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        longest = 0
        current=0
        length=0

        for num in nums_s:
            if num - 1 not in nums_s:
                current = num
                length = 1

            while current+1 in nums_s:
                current+=1
                length+=1
            longest=max(longest,length)

        return longest