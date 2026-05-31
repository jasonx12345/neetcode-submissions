class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap={} # initialie hash map
        
        tMap={}# initialize hash map
       
        for char in range(len(s)):
            if s[char] not in sMap: # we first create every value and set it to 0

                sMap[s[char]] = 0
            sMap[s[char]] += 1 # immeditly increment it if it appears, and additionally after that
        for char in range(len(t)):
            
            
            if t[char] not in tMap:
                tMap[t[char]] = 0
            tMap[t[char]] +=1
        if tMap == sMap:
            return True
        else:
            return False
            
            