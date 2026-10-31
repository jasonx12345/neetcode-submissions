class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mySet= set()

        for number in range(len(nums)):
            if nums[number] in mySet:
                return True
            else:
                mySet.add(nums[number])
        return False