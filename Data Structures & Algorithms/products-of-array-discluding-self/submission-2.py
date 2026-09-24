class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result =[1]* len(nums)
        leftProduct = 1
        for i in range (len(nums)):
            result[i] = leftProduct
            leftProduct *= nums[i]
        rightProduct = 1

        for i in range(len(nums) -1, -1, -1):# the -1, -1, -1 means start,stop, step. so start last stop before -1 so including 0, and incrmenet by -1
            result[i] *= rightProduct
            rightProduct *= nums[i]
        return result