class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation = 0
        n = len(nums)

        for i in range(n):
            # position is correct
            if nums[i] == 1:
                continue
            if i + 2 >= n:
                return -1
            
            nums[i] = 1 - nums[i]
            nums[i+ 1] = 1 - nums[i + 1]
            nums[i +2 ] = 1 - nums[i + 2] 
            operation += 1
        return operation 
            
