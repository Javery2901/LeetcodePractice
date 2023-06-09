import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.timestamp = -1
        self.follow_pointer = defaultdict(set)
        self.post = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append((self.timestamp, tweetId))  # post: {1: [(0, 1)]}
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        output = []
        if self.post[userId]:
            output.extend(self.post[userId][-1:-11:-1])
        if self.follow_pointer[userId]:
            for followee in self.follow_pointer[userId]:
                if self.post[followee]:
                    output.extend(self.post[followee][-1:-11:-1])
        heapq.heapify(output)
        count = 0
        while output and count < 10:
            time, tweet = heapq.heappop(output)
            res.append(tweet)
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_pointer[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follow_pointer[followerId]:
            return
        self.follow_pointer[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print('obj.follow_pointer =', obj.follow_pointer)
print('obj.post =', obj.post)
print()
print(obj.getNewsFeed(1))
obj.follow(1, 2)
print('obj.follow_pointer =', obj.follow_pointer)
print('obj.post =', obj.post)
print()
obj.postTweet(2, 6)
print('obj.follow_pointer =', obj.follow_pointer)
print('obj.post =', obj.post)
print()
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print('obj.follow_pointer =', obj.follow_pointer)
print('obj.post =', obj.post)
print()
print(obj.getNewsFeed(1))