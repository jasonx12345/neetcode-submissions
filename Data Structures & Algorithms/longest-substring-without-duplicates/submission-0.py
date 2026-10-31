class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to track unique characters currently inside our sliding window
        char_set = set()
        left = 0
        max_length = 0
        
        # Expand the window by moving the right pointer across the string
        for right in range(len(s)):
            
            # If the current character is already in our set, it's a duplicate.
            # Shrink the window from the left until the duplicate is removed.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the new, non-duplicate character to our set
            char_set.add(s[right])
            
            # Calculate the current window size (right - left + 1) and update max length
            max_length = max(max_length, right - left + 1)
            
        # Return the maximum length of a substring found without repeating characters
        return max_length