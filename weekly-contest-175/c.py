from heapq import heappush, heappop
from copy import deepcopy


class TweetCounts:

    def __init__(self):
        self.heap = []

    def recordTweet(self, tweetName: str, time: int) -> None:
        heappush(self.heap, (time, tweetName))

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:

        def do_it(interval):
            next_sec = startTime
            ans = []
            heap = deepcopy(self.heap)

            while heap and heap[0][0] <= endTime:
                count = 0
                next_sec += interval
                while heap and heap[0][0] < next_sec:
                    time, name = heappop(heap)
                    if name == tweetName and startTime <= time <= endTime:
                        count += 1
                ans.append(count)
            return ans

        if freq == 'minute':
            return do_it(60)
        elif freq == 'hour':
            return do_it(3600)
        else:  # day
            return do_it(3600 * 24)

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)