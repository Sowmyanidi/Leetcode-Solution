'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:  
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:  
                merged_intervals.append(interval)
        
        return merged_intervals

sol = Solution()
print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))