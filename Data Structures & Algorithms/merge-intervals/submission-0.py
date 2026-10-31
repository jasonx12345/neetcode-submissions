class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # given an array of intervals where start and end value, for each interval, we want to merge overlapping, and return non overlapping
        #intervals are givenin sorted order.
        #Input: intervals = [[1,3],[1,5],[6,7]]
        #Output: [[1,5],[6,7]]

        # we want to sort by the start value of each interval
        # then see if there is overlap


        #edge case if empty
        if not intervals:
            return []
        #sort intervals by their start times
        intervals.sort(key = lambda i : i[0])
        #start our output list with the first interval
        output = [intervals[0]]
        for start, end in intervals[1:]:

            # get the end time fothe last interval in our output list
            lastEnd = output [-1][1]

            # if there is overlap you merge them by updating the end time
            if start <= lastEnd:
                output[-1][1]= max(lastEnd, end)
            #non overlapping, just add new interval to output
            else:
                output.append([start, end])
        return output 

        