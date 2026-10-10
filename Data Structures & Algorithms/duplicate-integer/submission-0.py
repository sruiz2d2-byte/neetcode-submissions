class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        duplicates = []

        for num, count in num_counts.items():
            if count > 1:
                duplicates.append(num)

        if len(duplicates)!=0:
            return True
        return False