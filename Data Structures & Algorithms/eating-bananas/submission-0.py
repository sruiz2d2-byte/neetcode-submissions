from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1

        while left<right:
            mid=(left+right)//2

            hours=0
            for pile in piles:
                hours+=ceil(pile/mid)


            if hours<=h:
                right=mid
            else:
                left=mid+1
        
        return left
