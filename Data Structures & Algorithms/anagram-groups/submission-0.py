class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap={}
        for word in strs:
            sorted(word) # returns ["a", "e", "t"] 
            key = "".join(sorted(word))# "aet" — joins the letters into a string with no space
            if key not in HashMap:
                HashMap[key]= [] # if annogram doesnt exist, so we create an empty group to hold the list of words
            HashMap[key].append(word) # if anogram does exist
        return list(HashMap.values())