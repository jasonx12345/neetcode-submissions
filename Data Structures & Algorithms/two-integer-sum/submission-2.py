class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap ={}
        for i in range(len(nums)):
            myMap[nums[i]]= i 
            for j in range (len(nums)):
                if j != i and nums[j] + nums[i] == target:
                    
                    return [j,i] if j < i else [i, j]
      
        return False

            
                
        