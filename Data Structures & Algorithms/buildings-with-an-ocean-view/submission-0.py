
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        canSeeOcean = []
        max_height = 0
        for i in range(len(heights) -1, -1, -1):
            if heights[i] > max_height:
                canSeeOcean.append(i)
                max_height = heights[i]
        canSeeOcean.reverse()
        return canSeeOcean