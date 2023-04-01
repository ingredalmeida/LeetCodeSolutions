class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = list()
        aux = 0

        for i in range(len(nums)):
            aux += nums[i]
            runningSum.append(aux)

        return runningSum