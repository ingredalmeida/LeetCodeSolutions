class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        i = 0

        while i <= j:
            idx = (i+j) // 2

            if nums[idx] == target:
                return idx
            if nums[idx] < target:
                i = idx + 1
            if nums[idx] > target:
                j = idx - 1
        
        return -1