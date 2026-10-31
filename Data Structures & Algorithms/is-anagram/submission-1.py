class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        tMap = {}

        for char in range(len(s)):
            if s[char] not in sMap:
                sMap[s[char]]= 0
            sMap[s[char]]+=1

        for char in range(len(t)):
            if t[char] not in tMap:
                tMap[t[char]]= 0
            tMap[t[char]]+=1
        if tMap == sMap:
            return True
        else:
            return False

        