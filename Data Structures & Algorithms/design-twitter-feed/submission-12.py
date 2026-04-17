class PrioQueue:
    def __init__(self, nums):
        self.heap = []
        for time, _ in nums:
            self.insert(time)

    def size(self):
        return len(self.heap)
        
    def insert(self, val):
        self.heap.append(val)
        self.shift_up(self.size() - 1)
        
    def shift_up(self, i):
        while i > 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) //2], self.heap[i]
            i = (i - 1) // 2

    def pop(self):
        if self.size() > 0:
            val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap = self.heap[:-1]
            self.heapify()
            return val
        else:
            return -1

    def heapify(self):
        i = 0
        while 2*i+1 < self.size():
            lidx, ridx = 2*i+1, 2*i+2
            child = ridx if ridx < self.size() and self.heap[ridx] > self.heap[lidx] else lidx
            if self.heap[i] >= self.heap[child]:
                break
            else:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                i = child

class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.tweet_tracker = {}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_tracker[self.tweet_count] = tweetId
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = []
        if userId in self.follows:
            followees = self.follows[userId]
        tweets = []
        if userId in self.tweets:
            tweets += self.tweets[userId]

        for followeeId in followees:
            if followeeId in self.tweets:
                tweets += self.tweets[followeeId]

        newsFeed = []
        tweet_tracker = {}
        prio = PrioQueue(tweets)
        for i in range(10):
            val = prio.pop()
            if val == -1:
                break
            newsFeed.append(self.tweet_tracker[val])
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
