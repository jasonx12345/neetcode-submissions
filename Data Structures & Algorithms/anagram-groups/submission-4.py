class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        HashMap={}

        for words in strs:
            sorted(words) # this just make it like the same
            key = "".join(sorted(words)) # aet joings the letters into a 
            if key not in HashMap:
                HashMap[key] = []

            HashMap[key].append(words)
        return list(HashMap.values())
        