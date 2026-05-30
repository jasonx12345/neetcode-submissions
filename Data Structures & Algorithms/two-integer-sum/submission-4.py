class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oldMap = {} #val : index
        # creates the hashmap
        for i in range(len(nums)):
            oldMap[nums[i]]= i
        
        
        for j in range(len(nums)):
            difference = target - nums[j]
            if difference in oldMap and oldMap[difference] != j:
                return [j,oldMap[difference]]
        return False
