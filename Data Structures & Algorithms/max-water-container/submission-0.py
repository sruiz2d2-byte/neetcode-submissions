class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_water=0
        while i<j:
            water= (j - i) * min(heights[i], heights[j])
            if water>max_water:
                max_water=water
            min_bar=min(heights[i], heights[j])
            if min_bar==heights[i]:
                i+=1
            elif min_bar==heights[j]:
                j-=1

        return max_water

       