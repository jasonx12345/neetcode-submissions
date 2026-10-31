class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # you can return 2 arrays merged and sorted
        # but you also have empty space at the end of one of them so you dont make a temp array. 

        # last index nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            # compare the end of the 2 arrays
            if nums1[m-1] > nums2[n-1]:
                #if its bigger we slide it in
                nums1[last] = nums1[m-1]
                #move left in nums1 as you just usedits current number
                m -= 1
            else:
                # if they are the same value
                nums1 [last] = nums2[n-1]
                # moves left in nums2 as you just usedits current number
                n -= 1
            # move left in the desitnation slop of nums1 as you just filled the space at the end
            last -= 1
    # fill the front with the sorted part of the smaller array
        while n > 0:
            nums1[last] = nums2[n-1]
            n , last = n-1, last -1
        