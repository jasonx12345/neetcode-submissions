class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #we want to find the most frequent elements in an array k
        # create a hashmap
        HashMap={}
        # we put all values in hashmap
        for number in nums:
            if number not in HashMap: 
                # all keys have value to be 1
                HashMap[number] = 1
            if number in HashMap:
                # if we see it again we increment it
                HashMap[number] +=1
        
        # Sort the items based on their frequency (the value at index 1)
        sorted_items = sorted(HashMap.items(), key=lambda x: x[1])
        # Extract just the keys of the top k most frequent items from the end
        return [item[0] for item in sorted_items[-k:]]

            

