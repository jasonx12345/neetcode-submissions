class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we are given an array, we are look for a target value

        #if exists we return index if not return -1
        #keep div by 2
        #index of the 2 pointers
        left = 0
        right = len(nums) - 1

        while left <= right: 

            midway= (left + right ) //2
            # if the middle element is larger than the target, the target must be somewhere to the left
            if nums[midway]> target:
                # we make the new right one left of the midway point
                right = midway - 1
                # if the midway is smaller then the starget. because the array is sorted it must be somewhere to the right
            elif nums[midway] < target:
                # we make the new left value the midway + 1
                left = midway + 1
            else:
                return midway
        return -1