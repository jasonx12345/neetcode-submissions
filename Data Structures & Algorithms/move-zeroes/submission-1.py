class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Initialize the 'left' pointer to track where the next non-zero element should go
        left = 0
        
        # Iterate through the entire array using the 'right' pointer
        for right in range(len(nums)):
            
            # Check if the current element at 'right' is non-zero 
            # (In Python, any non-zero integer evaluates to True)
            if nums[right]:
                
                # Swap the non-zero element with the element at the 'left' pointer
                nums[left], nums[right] = nums[right], nums[left]
                
                # Advance the 'left' pointer forward to the next available slot
                left += 1
                
        # The function modifies the list in-place as requested by LeetCode, 
        # but returning nums is harmless if you want to test it locally.
        return nums