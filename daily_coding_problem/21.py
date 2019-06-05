'''
Problem # 21

Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if not intervals: return 0
        if not intervals[0]: return 1

        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        i = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                heappop(rooms)
            heappush(rooms, intervals[i][1])

        return len(rooms)
