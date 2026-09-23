class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        HashMap={}
        for number in nums:
            if number not in HashMap: 
                HashMap[number] = 1
            if number in HashMap:
                HashMap[number] +=1
        sortedNumbers = sorted(HashMap, key=HashMap.get)
        
        return sortedNumbers [-k:]# take the last k numbers

            

