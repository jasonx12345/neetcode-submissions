class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # creates the hashmap
        for i in range(len(nums)):
            map [nums[i]]= i
        #  loops through the items to see if the difference so the other half is in there.  
        for j in range (len(nums)):
            difference = target - nums[j]
             # if the value is in the map and is not the itself
            if difference in map and map[difference] != j:
                # we return the value and what adds to is
                return [j,map[difference]]
        return False # otherwise return false
                
        