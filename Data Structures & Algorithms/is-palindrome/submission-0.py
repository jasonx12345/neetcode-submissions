class Solution:
    def isPalindrome(self, s: str) -> bool:
        #given a string s it it a pallendrone, (same backwards as read forwards)
        # ignore upper lower case or spaces or special char

        newStr = ""
        # add if its in the alphanumeric to the new string
        for c in s:
            if c.isalnum():
                newStr +=c.lower()
        return newStr == newStr[::-1] # this reverses it in python
